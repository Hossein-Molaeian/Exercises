"""
Simple: write a function that checks whether a word or phrase is palindrome
(palindrome phrases read the same backwards as forwards)
"""


def is_palindrome(string):
    return string.lower() == string.lower()[::-1]
