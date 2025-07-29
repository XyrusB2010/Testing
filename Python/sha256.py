def decToBin(decimal):
    bin_list = []
    place = 1
    while place * 2 <= decimal:
        place = place * 2
    while place >= 1:
        if decimal >= place:
            bin_list.append('1')
            decimal = decimal - place
        else:
            bin_list.append('0')
        place = place / 2
    bin_list = ''.join(bin_list)
    while len(bin_list) < 64:
        bin_list = '0' + bin_list
    return bin_list

h0 = 0x6a09e667
h1 = 0xbb67ae85
h2 = 0x3c6ef372
h3 = 0xa54ff53a
h4 = 0x510e527f
h5 = 0x9b05688c
h6 = 0x1f83d9ab
h7 = 0x5be0cd19

message = input('Enter message to encrypt with SHA256: ')
message = ''.join(format(ord(char), '08b') for char in message)
messageLen = len(message)

message += '1'
while len(message) < 448:
    message += '0'
message += decToBin(messageLen)
print(len(message))