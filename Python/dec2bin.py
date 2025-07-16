decimal = input('Enter a number to convert to binary: ')
bin_list = []
place = 1
while not decimal.isdigit():
    print('Error: Your input is not a valid number.')
    decimal = input('Enter a number to convert to binary: ')
decimal = int(decimal)
while place * 2 <= decimal:
    place = place * 2
number = decimal
while place >= 1:
    if decimal >= place:
        bin_list.append(1)
        decimal = decimal - place
    else:
        bin_list.append(0)
    place = place / 2
if bin_list.count(1) % 2 != 0:
    bin_list.insert(0, 1)
else:
    bin_list.insert(0, 0)
print(f'{number} in binary (with even parity) is: ', end='')
print(*bin_list, sep='')
