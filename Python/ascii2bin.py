string = input('Enter 7 characters to convert to binary: ')
bin_list = []
parity_string = ''
place = 1
while len(string) != 7:
    print('Error: You have not entered 7 characters.')
    string = input('Enter 7 characters to convert to binary: ')
character = string
for i in range(len(string)):
    character = ord(string[i])
    bin_string = ''
    while place * 2 <= character:
        place = place * 2
    number = chr(character)
    while place >= 1:
        if character >= place:
            bin_string += '1'
            character = character - place
        else:
            bin_string += '0'
        place = place / 2
    bin_list.append(bin_string + ' ')
    if bin_string.count('1') % 2 != 0:
        parity_string += '1'
    else:
        parity_string += '0'
parity_string += ' '
bin_list.insert(0, parity_string)
print(f'"{string}" in binary (with even parity) is: ', end='')
print(*bin_list, sep='')
