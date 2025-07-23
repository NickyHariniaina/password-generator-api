import string
import random

"""
    Generate a randomized password with a length of 8 character or more, feel free to print.
    containing Uppercase, Lowercase letter, punctiation, and also numbers.
"""
def generate_password(length: int = 8) -> str:
    lowercase_letter: str = string.ascii_lowercase
    uppercase_letter: str = string.ascii_uppercase
    number: str = string.digits
    punctuation: str = string.punctuation
    characters: str = lowercase_letter + uppercase_letter + number + punctuation
    splited_password: list[str] = random.choices(characters, k=length)
    generated_password: str = "".join(splited_password)
    return generated_password


"""
    Check either a password is secure or not.
"""
def check_security(password: str) -> bool:
    has_enough_length: bool = len(password) >= 8
    has_digit: bool = any(letter in string.digits for letter in password)
    has_uppercase_letter: bool = any(letter in string.ascii_uppercase for letter in password)
    has_punc: bool = any(letter in string.punctuation for letter in password)
    return has_enough_length and has_digit and has_uppercase_letter and has_punc
