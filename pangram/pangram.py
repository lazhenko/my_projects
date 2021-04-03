from string import ascii_lowercase


def is_pangram(string):
    Alphabet = set(ascii_lowercase)
    return Alphabet.issubset(string.lower())
