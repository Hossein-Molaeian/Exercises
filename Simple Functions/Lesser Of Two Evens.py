"""
Very simple: Write a function that returns the lesser of two given numbers if both numbers
are even, but returns the greater if one or both numbers are odd
"""


def lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return min(a, b)
    return max(a, b)
