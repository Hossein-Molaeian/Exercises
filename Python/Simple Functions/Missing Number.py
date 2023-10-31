
"""
Write a function in 1 line to find missing numbers in a list.
"""


def get_missing_number(lst):
    return set(range(lst[len(lst)-1])[1:]) - set(lst)
