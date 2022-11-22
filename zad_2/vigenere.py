class EmptyStringError(Exception):
    def __init__(self, message="Argument string cannot be empty"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'


class InvalidLetterError(Exception):
    def __init__(self, word, message="Only capital letters form latin alhabet are acceptable"):
        self.word = word
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'


def is_correct(word):
    if len(word) == 0:
        raise EmptyStringError
    for letter in word:
        if not (ord(letter) in range(65, 91) or letter == " "):
            raise InvalidLetterError(word)


def get_encoded_letter(letter, key, position, key_len):
    return chr((ord(letter) + ord(key[position % key_len]) - 2*ord("A")) % 26 + ord('A'))


def encrypt_vigenere2(key, plaintext):
    is_correct(key)
    is_correct(plaintext)
    key.replace(" ", "")
    encrypted = ""
    i = 0
    for letter in plaintext:
        if letter == " ":
            encrypted += " "
        else:
            encrypted += get_encoded_letter(letter, key, i, len(key))
            # i increments only if letter is not a space
            i += 1
    return encrypted


def decrypt_vigenere2(key, ciphertext):
    key.replace(" ", "")
    reversed = ""
    for letter in key:
        reversed += chr((26 - ord(letter) + ord('A')) % 26 + ord('A'))
    return encrypt_vigenere2(reversed, ciphertext)
