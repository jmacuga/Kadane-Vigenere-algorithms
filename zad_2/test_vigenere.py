
from vigenere import EmptyStringError, InvalidLetterError, encrypt_vigenere2, is_correct, decrypt_vigenere2
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


def test_encrypt_vigenere2_empty_key():
    key = ""
    plaintext = "SIEMA"
    with pytest.raises(EmptyStringError):
        encrypt_vigenere2(key, plaintext)


def test_encrypt_vigenere_one_letter():
    key = "K"
    plaintext = "L"
    assert encrypt_vigenere2(key, plaintext) == "V"


def test_encrypt_vigenere_same_len():
    key = "KEY"
    plaintext = "LEN"
    assert encrypt_vigenere2(key, plaintext) == "VIL"


def test_encrypt_vigenere_longer_text():
    key = "KEY"
    plaintext = "LENGTH"
    assert encrypt_vigenere2(key, plaintext) == "VILQXF"


def test_decrypt_vigenere_one_letter():
    key = "T"
    ciphertext = "M"
    assert decrypt_vigenere2(key, ciphertext) == "T"


def test_decrypt_vigenere_word():
    key = "TAJNE"
    ciphertext = "MOSRWM"
    assert decrypt_vigenere2(key, ciphertext) == "TOJEST"


def test_encode_spaces():
    text = "TOJEST BARDZO TAJNY TEKST"
    key = "TAJNE"
    assert encrypt_vigenere2(key, text) == "MOSRWM BJEHSO CNNGY CROLT"


def test_decode_spaces():
    cipher = "MOSRWM BJEHSO CNNGY CROLT"
    key = "TAJNE"
    assert decrypt_vigenere2(key, cipher) == "TOJEST BARDZO TAJNY TEKST"
