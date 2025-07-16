def encrypt():
    shift = ''
    while not shift.isdigit():
        shift = input('Enter number of shifts: ')
    shift = int(shift)
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    decrypted = input('Enter message to encrypt: ').upper()
    encrypted = []
    for i in range(len(decrypted)):
        if decrypted[i].isalpha() and not decrypted[i] == ' ':
            char = alphabet.index(decrypted[i]) + shift
            while char > 25:
                char -= 26
            encrypted.append(alphabet[char])
        elif decrypted[i].isnumeric():
            char = numbers.index(decrypted[i]) + shift
            while char > 9:
                char -= 10
            encrypted.append(numbers[char])
        else:
            encrypted.append(decrypted[i])
    print(*encrypted, sep='')

def decrypt():
    shift = ''
    while not shift.isdigit():
        shift = input('Enter number of shifts: ')
    shift = int(shift)
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    encrypted = input('Enter message to decrypt: ').upper()
    decrypted = []
    for i in range(len(encrypted)):
        if encrypted[i].isalpha() and not encrypted[i] == ' ':
            char = alphabet.index(encrypted[i]) - shift
            while char < 0:
                char += 26
            decrypted.append(alphabet[char])
        elif encrypted[i].isnumeric():
            char = numbers.index(encrypted[i]) - shift
            while char < 0:
                char += 10
            decrypted.append(numbers[char])
        else:
            decrypted.append(encrypted[i])
    print(*decrypted, sep='')

def solve():
    from english_words import get_english_words_set as dictionary
    wordList = list(dictionary(['web2']))
    for i in range(len(wordList)):
        wordList[i] = wordList[i].upper()
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    encrypted = input('Enter message to solve: ').upper()
    attempts = []

    for shift in range(26):
        decrypted = []
        for i in range(len(encrypted)):
            if encrypted[i].isalpha() and not encrypted[i] == ' ':
                char = alphabet.index(encrypted[i]) - shift
                while char < 0:
                    char += 26
                decrypted.append(alphabet[char])
            elif encrypted[i].isnumeric():
                char = numbers.index(encrypted[i]) - shift
                while char < 0:
                    char += 10
                decrypted.append(numbers[char])
            else:
                decrypted.append(encrypted[i])
        attempts.append(''.join(decrypted))
    
    for i in attempts:
        if attempts[i] in wordList:
            print(f'Match found: {attempts[i]}')
        else:
            print(f'No match found, but you can look at these possibilities: {attempts}')

import sys
option = ''
while not option.isdigit():
    option = input('Press 1 for encryption | Press 2 for decryption | Press 3 for solving: ')
option = int(option)
if option == 1: encrypt()
elif option == 2: decrypt()
elif option == 3: solve()
else:
    print(f'Enter "1" or "2"! Not {option}!', file=sys.stderr)
    exit()
