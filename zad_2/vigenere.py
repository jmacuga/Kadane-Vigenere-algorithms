class LenghtError(Exception):
    pass


class InvalidLetterError(Exception):
    pass


def is_correct(word):
    if len(word) == 0:
        raise LenghtError
    for letter in word:
        if not (ord(letter) in range(65, 91) or letter == " "):
            raise InvalidLetterError(word)


def encrypt_vigenere2(key, plaintext):
    is_correct(key)
    key.replace(" ", "")
    is_correct(plaintext)
    encrypted = ""
    key_len = len(key)
    i = 0
    for letter in plaintext:
        if letter == " ":
            encrypted += " "
        else:
            encrypted += chr((ord(letter) +
                              ord(key[i % key_len]) - 2*ord("A")) % 26 + ord('A'))
            i += 1
    return encrypted


def decrypt_vigenere2(key, ciphertext):
    key.replace(" ", "")
    reversed = ""
    for letter in key:
        reversed += chr((26 - ord(letter) + ord('A')) % 26 + ord('A'))
    return encrypt_vigenere2(reversed, ciphertext)
