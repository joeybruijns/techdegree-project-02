import string

from ciphers import Cipher


class Keyword(Cipher):
    def __init__(self):
        """Init methods contains two alphabet lists, one original
        and one to modify
        """
        self.plain_alphabet = list(string.ascii_uppercase)
        self.keyword_alphabet = list(string.ascii_uppercase)

    def get_keyword(self, keyword):
        """Takes a keyword from the user and modifies the
        keyword_alphabet list
        """
        self.keyword = keyword.upper()
        key_list = [item for item in self.keyword]
        # reveres the key_list so we append in the right order
        key_list = key_list[::-1]
        try:
            for char in key_list:
                index = self.keyword_alphabet.index(char)
                value = self.keyword_alphabet.pop(index)
                self.keyword_alphabet.insert(0, value)
        except ValueError:
            pass

    def encrypt(self, text):
        """Takes a string message and encrypts it using the index
        values of the keyword_alphabet list
        """
        text = text.upper()
        keyword_code = []

        for item in text:
            try:
                index = self.plain_alphabet.index(item)
            except ValueError:
                keyword_code.append(item)
            else:
                keyword_code.append(self.keyword_alphabet[index])
        return ''.join(keyword_code)

    def decrypt(self, text):
        """Takes an encrypted message and decrypts it using the index
        values of the original plain_alphabet list
        """
        self.text = text.upper()
        decrypt_code = []

        for item in self.text:
            try:
                index = self.keyword_alphabet.index(item)
            except ValueError:
                decrypt_code.append(item)
            else:
                decrypt_code.append(self.plain_alphabet[index])
        return ''.join(decrypt_code)
