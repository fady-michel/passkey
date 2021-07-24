from sys import argv
from itertools import cycle


class Key(object):
    def __init__(self, operation: str, user_input : str) -> None:
        super().__init__()
        self.OFFSET = 33
        self.operation = operation
        self.key = 'MySecretKey'
        self.user_input = user_input
        
        self.translate()

    def translate(self) -> None:
        if self.operation.lower() == 'encrypt':
            xored = ''.join([chr((ord(i) ^ ord(k)) + self.OFFSET) for i, k in zip(self.user_input, cycle(self.key))])
        elif self.operation.lower() == 'decrypt':
            xored = ''.join([chr((ord(i) - self.OFFSET) ^ ord(k))  for i, k in zip(self.user_input, cycle(self.key))])
        else:
            print('Invalid operation. Only encrypt and decrypt are allowed.')
            return
        
        # for i, k in zip(self.user_input, cycle(self.key)):
        #     print(i, k, i ^ k)
        #     print(chr(i ^ k).encode())

        print(xored)

my_key = Key(operation=argv[1], user_input=argv[2])