"""
Write a function to check whether a string is pangram or not.
(Pangram string is a string that contains all letters in the alphabet).
"""
import string


def is_pangram(input_string):

    unique_letters = set(input_string)
    alphabet = string.ascii_letters + " "
    for letter in unique_letters:
        if letter in alphabet:
            pass
        else:
            return "Is not pangram."
    return "Is pangram."


print(is_pangram("The quick brown fox jumps over a lazy dog"))
