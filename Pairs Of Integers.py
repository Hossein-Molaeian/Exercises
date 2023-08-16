"""
Find pairs of integers in a list so that their sum is equal to integer x
"""


def find_pairs(lst, x):
    pairs = []
    for (i, element1) in enumerate(lst):
        for (j, element2) in enumerate(lst):
            if element1 + element2 == x:
                pairs.append((element1, element2))
    return pairs


print(find_pairs([1, 3, 5, 7, 9], 10))
