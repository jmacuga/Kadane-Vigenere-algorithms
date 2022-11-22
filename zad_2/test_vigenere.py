
from vigenere import EmptyStringError, InvalidLetterError, encrypt_vigenere, is_correct, decrypt_vigenere
from vigenere import get_encoded_letter, get_reversed_letter
import pytest


def test_is_correct_empty_key():
    key = ""
    with pytest.raises(EmptyStringError):
        is_correct(key)


def test_is_correct_empty_text():
    plaintext = ""
    with pytest.raises(EmptyStringError):
        is_correct(plaintext)


def test_is_correct_lowercase1():
    key = "a"
    with pytest.raises(InvalidLetterError):
        is_correct(key)


def test_is_correct_invalid_symbol():
    key = "ź"
    with pytest.raises(InvalidLetterError):
        is_correct(key)


def test_is_correct_symbol():
    key = ";"
    with pytest.raises(InvalidLetterError):
        is_correct(key)


def test_is_correct_polish_letter():
    plaintext = "Ż"
    with pytest.raises(InvalidLetterError):
        is_correct(plaintext)


def test_is_correct_symbol_pass():
    key = "A"
    plaintext = "Z"
    is_correct(key)
    is_correct(plaintext)


def test_get_encoded_letter_one_letter():
    key = 'A'
    plaintext = "Z"
    assert get_encoded_letter(plaintext, key, 0, 1) == 'Z'


def test_get_encoded_letter_one_letter2():
    key = 'P'
    plaintext = "H"
    assert get_encoded_letter(plaintext, key, 0, 1) == 'W'


def test_get_encoded_letter_word():
    key = 'KEY'
    plaintext = "HASLO"
    position = 3
    assert get_encoded_letter(
        plaintext[position], key, position, len(key)) == 'V'


def test_get_encoded_letter_word2():
    key = 'KEY'
    plaintext = "HASLO"
    position = 1
    assert get_encoded_letter(
        plaintext[position], key, position, len(key)) == 'E'


def test_get_reversed_letter():
    key = 'K'
    assert get_reversed_letter(key) == 'Q'


def test_get_reversed_letter2():
    key = 'A'
    assert get_reversed_letter(key) == 'A'


def test_get_reversed_letter3():
    key = 'Z'
    assert get_reversed_letter(key) == 'B'


def test_get_reversed_letter4():
    key = 'R'
    assert get_reversed_letter(key) == 'J'


def test_encrypt_vigenere_empty_key():
    key = ""
    plaintext = "SIEMA"
    with pytest.raises(EmptyStringError):
        encrypt_vigenere(key, plaintext)


def test_encrypt_vigenere_one_letter():
    key = "K"
    plaintext = "L"
    assert encrypt_vigenere(key, plaintext) == "V"


def test_encrypt_vigenere_same_len():
    key = "KEY"
    plaintext = "LEN"
    assert encrypt_vigenere(key, plaintext) == "VIL"


def test_encrypt_vigenere_longer_text():
    key = "KEY"
    plaintext = "LENGTH"
    assert encrypt_vigenere(key, plaintext) == "VILQXF"


def test_decrypt_vigenere_one_letter():
    key = "T"
    ciphertext = "M"
    assert decrypt_vigenere(key, ciphertext) == "T"


def test_decrypt_vigenere_word():
    key = "TAJNE"
    ciphertext = "MOSRWM"
    assert decrypt_vigenere(key, ciphertext) == "TOJEST"


def test_encode_spaces():
    text = "TOJEST BARDZO TAJNY TEKST"
    key = "TAJNE"
    assert encrypt_vigenere(key, text) == "MOSRWM BJEHSO CNNGY CROLT"


def test_decode_spaces():
    cipher = "MOSRWM BJEHSO CNNGY CROLT"
    key = "TAJNE"
    assert decrypt_vigenere(key, cipher) == "TOJEST BARDZO TAJNY TEKST"
