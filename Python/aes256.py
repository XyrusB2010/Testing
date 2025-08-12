message = input('Enter a message to encrypt: ')
key = input('Enter AES256 key: ')
mode = int(input('Enter mode for encryption (1 - CBC | 2 - ECB | 3 - GCM): '))
splitMessage = []
encodedMessage = message.encode('utf-8').hex().upper()

if len(encodedMessage) > 32:
    print(f'Message is {len(message)} bytes long. Slicing into 16 byte chunks...')
    splitMessage = [encodedMessage[i:i+32] for i in range(0, len(encodedMessage), 32)]
else:
    splitMessage.append(encodedMessage)

while len(splitMessage[-1]) < 32:
    splitMessage[-1] += '05'

if mode == 1:
    print('CBC encryption selected.')
elif mode == 2:
    print('ECB encryption selected.')
elif mode == 3:
    print('GCM encryption selected.')