from ciphers import Cipher


class Polybius(Cipher):
    def __init__(self):
        """Init method holds a multidimensional list with
        a grid of letters en string numbers
        """
        self.crypto_grid = [
            ['A', 'B', 'C', 'D', 'E', 'F'],
            ['G', 'H', 'I', 'J', 'K', 'L'],
            ['M', 'N', 'O', 'P', 'Q', 'R'],
            ['S', 'T', 'U', 'V', 'W', 'X'],
            ['Y', 'Z', '1', '2', '3', '4'],
            ['5', '6', '7', '8', '9', '0']
        ]

    def find_index(self, list, elem):
        """Used in the encrypt method. Takes a character and gives
        back a string representation of a double digit number
        """
        secret_num = ""
        for row, item in enumerate(list):
            try:
                column = item.index(elem)
            except ValueError:
                continue
            else:
                secret_num += str(row)
                secret_num += str(column)
            return secret_num

    def find_letter(self, num1, num2):
        """returns the correct letter using the two index positions"""
        return self.crypto_grid[num1][num2]

    def encrypt(self, string):
        """Encrypts characters to string numbers
        using the find_index method above
        """
        string = string.upper()
        secret_code = ""
        for item in string:
            try:
                if item != " ":
                    secret_code += self.find_index(self.crypto_grid, item)
                else:
                    secret_code += " "
            except TypeError:
                pass
        return secret_code

    def decrypt(self, string):
        """Decrypts a message by taking two index positions and returns
        the value from the multidimensional list
        """
        string = string.split()
        decoded = []
        for item in string:
            try:
                # zip() used to get back both the index for the
                # inner list and the outer list
                for num1, num2 in zip(item[::2], item[1::2]):
                    decoded.append(self.find_letter(int(num1), int(num2)))

            except ValueError:
                pass
            decoded.append(" ")
        return "".join(decoded)
