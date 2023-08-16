
"""
the first set contains all numbers from 1 to the last
element of the input 'lst'. The set difference operation
('-') is done to print the missing numbers in 'lst'
"""


def get_missing_number(lst):
    return set(range(lst[len(lst)-1])[1:]) - set(lst)
