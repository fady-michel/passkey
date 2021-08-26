from sys import argv
from itertools import cycle
import os


class Key(object):
    def __init__(self, operation: str, user_input: str) -> None:
        super().__init__()
        self.OFFSET = 33
        self.operation = operation
        self.key = os.environ.get('PASS_KEY') or 'My_SECRET'
        self.user_input = user_input
        self.translate()

    def translate(self) -> None:
        if self.operation.lower() == 'encrypt':
            xored = ''.join([chr((ord(i) ^ ord(k)) + self.OFFSET)
                             for i, k in zip(self.user_input, cycle(self.key))])
        elif self.operation.lower() == 'decrypt':
            xored = ''.join([chr((ord(i) - self.OFFSET) ^ ord(k))
                             for i, k in zip(self.user_input, cycle(self.key))])
        else:
            print('Invalid operation. Only encrypt and decrypt are allowed.')
            return

        # for i, k in zip(self.user_input, cycle(self.key)):
        #     print(i, k, i ^ k)
        #     print(chr(i ^ k).encode())
        indicator = ':O' if self.key == 'My_SECRET' else ''
        print(xored, indicator)


help_msg = """Usage: translate [OPERATION]
Operation:
    encrypt     to encrypt password using the key
    decrypt     to decrypt the text using the key
"""

if len(argv) != 2:
    print('Invalid input')
    print(help_msg)
else:
    if argv[1].lower() not in ['encrypt', 'decrypt']:
        print('Invalid input')
        print(help_msg)
    else:
        user_input = input(f'Enter the text for {argv[1]} operation > ')
        Key(operation=argv[1], user_input=user_input)
