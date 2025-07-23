def asciiToBin(string):
    bin_list = []
    place = 1
    character = string
    for i in range(len(string)):
        character = ord(string[i])
        bin_string = ''
        while place * 2 <= character:
            place = place * 2
        while place >= 1:
            if character >= place:
                bin_string += '1'
                character = character - place
            else:
                bin_string += '0'
            place = place / 2
        bin_list.append(bin_string)
    bin_list = ''.join(bin_list)
    return(bin_list)

h0 = 0x6a09e667
h1 = 0xbb67ae85
h2 = 0x3c6ef372
h3 = 0xa54ff53a
h4 = 0x510e527f
h5 = 0x9b05688c
h6 = 0x1f83d9ab
h7 = 0x5be0cd19

message = input('Enter message to encrypt with SHA256: ')
binMessage = asciiToBin(message)
messageList = []

if len(binMessage) > 512:
    print(f'Your message is {len(binMessage)} bits long, which is more than 512 bits. Slicing into 512-bit blocks...')
    for i in range(0, len(binMessage), 512):
        messageList.append(binMessage[i:i+512])
    messageList[-1] += '1'
    for i in range(512 - len(binMessage[-1])):
        messageList[-1] += '0'
elif len(binMessage) > 64:
    print(f'Your message is {len(binMessage)} bits long, which is more than 64 bits. Padding to 512 bits...')
    binMessage += '1'
    for i in range(512 - len(binMessage)):
        binMessage += '0'
else:
    print(f'Your message is {len(binMessage)} bits long. Padding to 64 bits...')
    binMessage += '1'
    for i in range(64 - len(binMessage)):
        binMessage += '0'
print(len(messageList[-1]))