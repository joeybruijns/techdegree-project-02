import string

from ciphers import Cipher


class Atbash(Cipher):
    def __init__(self):
        self.alphabet = list(string.ascii_uppercase)
        self.reversed_alphabet = self.alphabet[::-1]

    def encrypt(self, text):
        """Takes a message and encrypts it using the index position
        of the reversed_alphabet list
        """
        text = text.upper()
        atbash_code = []

        for item in text:
            try:
                index = self.alphabet.index(item)
            except ValueError:
                atbash_code.append(item)
            else:
                atbash_code.append(self.reversed_alphabet[index])
        return ''.join(atbash_code)

    def decrypt(self, text):
        """Decrypts a message provided by the user using the index
        positions of the reversed_alphabet list
        """
        text = text.upper()
        atbash_code = []

        for item in text:
            try:
                index = self.reversed_alphabet.index(item)
            except ValueError:
                atbash_code.append(item)
            else:
                atbash_code.append(self.alphabet[index])
        return ''.join(atbash_code)
