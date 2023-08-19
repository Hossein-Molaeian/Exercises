"""
Medium: given a list of ints, return True if the array contains a 3 next to a 3 somewhere
"""


def find_33(lst):
    for i in range(0, len(lst)-1):
        if lst[i] == 3 and lst[i+1] == 3:
            return True
    return False
