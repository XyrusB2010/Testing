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
    # numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    encrypted = input('Enter message to solve: ').upper()
    encryptedList = encrypted.split()
    attempts = []
    decryptedList = []

    for word in encryptedList:
        attempts = []
        foundMatch = None
        for shift in range(26):
            decrypted = []
            for i in range(len(word)):
                if word[i].isalpha() and not word[i] == ' ':
                    char = alphabet.index(word[i]) - shift
                    while char < 0:
                        char += 26
                    decrypted.append(alphabet[char])
                # elif word[i].isnumeric():
                #     char = numbers.index(word[i]) - shift
                #     while char < 0:
                #         char += 10
                #     decrypted.append(numbers[char])
                else:
                    decrypted.append(word[i])
            attempts.append(''.join(decrypted))
        for attempt in attempts:
            if attempt in wordList:
                decryptedList.append(attempt)
                print(f'Match found: {attempt}')
                print(f'Number of shifts used: {attempts.index(attempt)}')
                print(f'Other possibilities: {attempts} \n')
                foundMatch = True
        if foundMatch != True:
                print(f'No match found, but here are all possibilities: {attempts} \n')

    print(f'Fully decoded phrase: {' '.join(decryptedList)}')

import sys
option = ''
while not option.isdigit():
    option = input('Press 1 for encryption | Press 2 for decryption | Press 3 for solving: ')
option = int(option)
if option == 1: encrypt()
elif option == 2: decrypt()
elif option == 3: solve()
else:
    print(f'Enter "1", "2" or "3"! Not {option}!', file=sys.stderr)
    exit()
