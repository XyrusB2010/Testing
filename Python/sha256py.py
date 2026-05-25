#!/usr/bin/env python3
import argparse
import sys
import requests
import os

def rotr(input, bits):
    return ((input >> bits) | (input << (32 - bits))) & 0xFFFFFFFF

def shiftr(input, bits):
    return input >> bits

def sigma0(n):
    return rotr(n, 7) ^ rotr(n, 18) ^ shiftr(n, 3)

def sigma1(n):
    return rotr(n, 17) ^ rotr(n, 19) ^ shiftr(n, 10)

def add32(*args):
    return sum(args) & 0xFFFFFFFF

h0 = 0x6a09e667
h1 = 0xbb67ae85
h2 = 0x3c6ef372
h3 = 0xa54ff53a
h4 = 0x510e527f
h5 = 0x9b05688c
h6 = 0x1f83d9ab
h7 = 0x5be0cd19

K = [
    0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5,
    0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
    0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3,
    0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
    0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc,
    0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
    0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7,
    0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
    0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13,
    0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
    0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3,
    0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
    0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5,
    0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
    0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208,
    0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
]

def sha256_hash(message_bytes):
    message = ''.join(format(byte, '08b') for byte in message_bytes)
    messageLen = len(message)
    message += '1'
    while (len(message) + 64) % 512 != 0:
        message += '0'
    message += format(messageLen, '064b')
    chunks = [message[i:i+512] for i in range(0, len(message), 512)]
    hash_pieces = [h0, h1, h2, h3, h4, h5, h6, h7]
    for chunk in chunks:
        W = [int(chunk[i:i+32], 2) for i in range(0, 512, 32)]
        for i in range(16, 64):
            s0 = sigma0(W[i - 15])
            s1 = sigma1(W[i - 2])
            W.append(add32(W[i - 16], s0, W[i - 7], s1))
        a, b, c, d, e, f, g, h = hash_pieces
        for i in range(64):
            S1 = rotr(e, 6) ^ rotr(e, 11) ^ rotr(e, 25)
            ch = (e & f) ^ ((~e) & g)
            temp1 = add32(h, S1, ch, K[i], W[i])
            S0 = rotr(a, 2) ^ rotr(a, 13) ^ rotr(a, 22)
            maj = (a & b) ^ (a & c) ^ (b & c)
            temp2 = add32(S0, maj)
            h = g
            g = f
            f = e
            e = add32(d, temp1)
            d = c
            c = b
            b = a
            a = add32(temp1, temp2)
        hash_pieces = [
            add32(hash_pieces[0], a),
            add32(hash_pieces[1], b),
            add32(hash_pieces[2], c),
            add32(hash_pieces[3], d),
            add32(hash_pieces[4], e),
            add32(hash_pieces[5], f),
            add32(hash_pieces[6], g),
            add32(hash_pieces[7], h)
        ]
    return ''.join(format(x, '08x') for x in hash_pieces)

def main():
    parser = argparse.ArgumentParser(
    description=r'''
 $$$$$$\  $$\   $$\  $$$$$$\   $$$$$$\  $$$$$$$\   $$$$$$\  
$$  __$$\ $$ |  $$ |$$  __$$\ $$  __$$\ $$  ____| $$  __$$\ 
$$ /  \__|$$ |  $$ |$$ /  $$ |\__/  $$ |$$ |      $$ /  \__|
\$$$$$$\  $$$$$$$$ |$$$$$$$$ | $$$$$$  |$$$$$$$\  $$$$$$$\  
 \____$$\ $$  __$$ |$$  __$$ |$$  ____/ \_____$$\ $$  __$$\ 
$$\   $$ |$$ |  $$ |$$ |  $$ |$$ |      $$\   $$ |$$ /  $$ |
\$$$$$$  |$$ |  $$ |$$ |  $$ |$$$$$$$$\ \$$$$$$  | $$$$$$  |
 \______/ \__|  \__|\__|  \__|\________| \______/  \______/ py''',
    formatter_class=argparse.RawTextHelpFormatter
)
    parser.add_argument('-f', '--file', type=str, help='File to hash')
    parser.add_argument('-c', '--check', type=str, help='Hash string to check against')
    parser.add_argument('-u', '--url', type=str, help='Hash file from URL')
    parser.add_argument('-s', '--save', type=str, help='Save generated hash as a file')
    parser.add_argument('-v', '--verify', type=str, help='.csv file to verify')
    parser.add_argument('--salt', type=str, help='Append a salt to your input before hashing')
    parser.add_argument('--bruteforce', type=str, help='Attempt to decode the phrase using a file containing possible phrases, enter "ENGLISHDICTIONARY" to attempt a bruteforce hash using the English dictionary assuming the phrase is a single English word')
    parser.add_argument('text', nargs='*', help='Text to hash if no file is provided')
    args = parser.parse_args()
    if not args.file and not args.url and not args.text and not args.check and not args.verify:
        print("Error: You must provide either text to hash, a file with -f, a URL with -u, or a .csv file with -v.")
        parser.print_help()
        sys.exit(1)
    if args.file:
        try:
            with open(args.file, 'rb') as file:
                message_bytes = file.read()
        except FileNotFoundError:
            print(f"Error: File '{args.file}' not found.")
            sys.exit(1)
        except Exception as e:
            print(f"Error reading file '{args.file}': {e}")
            sys.exit(1)
    elif args.url:
        try:
            response = requests.get(args.url)
            response.raise_for_status()
            message_bytes = response.content
        except Exception as e:
            print(f"Error fetching URL '{args.url}': {e}")
            sys.exit(1)
    elif args.salt:
        args.text[-1] += args.salt
        message_bytes = ' '.join(args.text).encode('utf-8')
    else:
        message_bytes = ' '.join(args.text).encode('utf-8')
    output = sha256_hash(message_bytes)
    if args.check:
        if '.sha256sum' in args.check:
            with open(args.check, 'r') as file:
                contents = file.read().split(',')
            hash = contents[0]
            filename = contents[-1]
            with open(filename, 'rb') as file:
                message_bytes = file.read()
            output = sha256_hash(message_bytes)
            if output == hash:
                print("Success: Hashes match.")
                sys.exit()
            else:
                print("Failure: Hashes do not match.")
                print(f"Expected: {args.check}")
                print(f"Computed: {output}")
                sys.exit(1)
        else:
            if output == args.check:
                print("Success: Hashes match.")
                sys.exit(0)
            else:
                print("Failure: Hashes do not match.")
                print(f"Expected: {args.check}")
                print(f"Computed: {output}")
                sys.exit(1)
    elif args.save:
        filename = args.save.strip()
        if not filename:
            print('Error: Please enter a valid filename.')
            sys.exit(1)
        if '.csv' in filename:
            print('CSV file detected!')
            with open(filename, 'r') as file:
                validHeader = file.readline().strip() == 'hash,phrase'
                contents = file.readlines()
            if not validHeader:
                print('Warning: File is not a valid format.')
                contents.insert(0, 'hash,phrase')
                with open(filename, 'w') as file:
                    file.write('\n'.join(contents))
        with open(filename, 'a') as file:
            file.write(f'\n{output},{' '.join(args.text)}')
        print(f'SHA256 hash saved to {filename}.')
    elif args.verify:
        try:
            with open(args.verify, 'r') as file:
                checklist = file.read().splitlines()
        except FileNotFoundError:
            print(f"Error: File '{args.verify}' not found.")
            sys.exit(1)
        except Exception as e:
            print(f"Error reading file '{args.verify}': {e}")
            sys.exit(1)
        for i in range(len(checklist)):
            checklist[i] = checklist[i].split(',')
        hashPassed = 0
        totalHashes = len(checklist)
        for line in checklist:
            if ','.join(line) == "hash,phrase":
                totalHashes -= 1
                continue
            hash = line[0]
            message = line[-1]
            encoded = message.encode('utf-8')
            if hash != sha256_hash(encoded):
                print(f'{message} - Expected {sha256_hash(encoded)}, not {hash} (FAIL)')
            else:
                print(f'{message} - {hash} (PASS)')
                hashPassed += 1
        print(f'{hashPassed} of {totalHashes} hashes passed.')
    elif args.bruteforce:
        attempts = []
        if args.bruteforce == 'ENGLISHDICTIONARY':
            if input('Are you really sure you want to do this? (y/N): ').strip() == 'y':
                englishDictionary = "https://raw.githubusercontent.com/dwyl/english-words/refs/heads/master/words_alpha.txt"
                attempts = requests.get(englishDictionary).content.decode('utf-8').splitlines()
            else:
                print('Aborting.')
                sys.exit(0)
        else:
            try:
                with open(args.bruteforce, 'r') as file:
                    attempts = file.read().splitlines()
            except FileNotFoundError:
                print(f"Error: File '{args.bruteforce} not found.")
            except Exception as e:
                print(f"Error reading file '{args.bruteforce}': {e}")
        for attempt in attempts:
            encoded = attempt.encode('utf-8')
            if sha256_hash(encoded) == ''.join(args.text):
                print(f'Attempting {attempt}: PASS')
                print(f'Found match: {attempt} - {sha256_hash(encoded)} at {attempts.index(attempt) + 1}/{len(attempts)} phrases. (PASS)')
                sys.exit(0)
            else:
                print(f'Attempting {attempt}: FAIL')
        print(f'No matches found out of {len(attempts)} phrases. (FAIL)')
    else:
        print(output)
if __name__ == "__main__":
    main()
