from atbash import Atbash
from keywords import Keyword
from polybius import Polybius


def encrypt_it(cipher):
    """Takes a message and returns the encrypted version"""
    message = input("What is your message? ")
    return "Here's your secret message: " + cipher.encrypt(message) + "\n"


def decrypt_it(cipher):
    """Takes a encrypted message and decrypts it
    using the right cipher
    """
    message = input("What message do you want to decrypt? ")
    return "Here's your decrypted message: " + cipher.decrypt(message) + "\n"


def user_input():
    return input("Would you like to encrypt or decrypt? ").upper()


print("Welcome, let's create a secret message!\n")
print("""You can choose from 3 different ciphers:
- Atbash
- Keyword
- Polybius\n""")


def script():
    """Runs the script for the command line menu, asking the user
    for the message to encrypt/decrypt"""
    atb = Atbash()
    key = Keyword()
    poly = Polybius()
    choose_cipher = input("Which one do you want to use? ")

    if choose_cipher.upper() == "ATBASH":
        action = user_input()
        if action.upper() == "ENCRYPT":
            print(encrypt_it(atb))
        elif action.upper() == "DECRYPT":
            print(decrypt_it(atb))
        else:
            print("Sorry I didn't understand that...\n")
    elif choose_cipher.upper() == "KEYWORD":
        our_keyword = input("What keyword would you like to use? ")
        key.get_keyword(our_keyword)
        action = user_input()
        if action.upper() == "ENCRYPT":
            print(encrypt_it(key))
        elif action.upper() == "DECRYPT":
            print(decrypt_it(key))
        else:
            print("Sorry I didn't understand that...\n")
    elif choose_cipher.upper() == "POLYBIUS":
        action = user_input()
        if action.upper() == "ENCRYPT":
            print(encrypt_it(poly))
        elif action.upper() == "DECRYPT":
            print(decrypt_it(poly))
        else:
            print("Sorry I didn't understand that...\n")
    else:
        print("I didn't understand that, please try again!\n")

    # ask the user if he wants to encrypt/decrypt something else
    encrypt_more = input("Encrypt or decrypt something else? Y/N ")
    if encrypt_more.upper() != "N":
        script()
    else:
        print("Thank you, bye!")

script()
