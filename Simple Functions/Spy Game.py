"""
Hard: write a function that takes in a list of integers and returns True
if it contains 007 in order anywhere in the list (even if 007 is separated
in order between numbers)
"""


def spy_game(arr):
    code = [0, 0, 7, "x"]
    for num in arr:
        if num == code[0]:
            code.pop(0)
    return len(code) == 1
