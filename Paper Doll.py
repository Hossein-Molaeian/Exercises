"""
Medium: given a string, return a string where for 
every character in the original there are three characters
"""


def paper_doll(string):
    lst = []
    for s in string:
        lst.append(s*3)
    return "".join(lst)
