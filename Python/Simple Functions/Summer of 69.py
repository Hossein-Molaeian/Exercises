"""
Return the sum of the numbers in the array, except ignore 
sections of numbers starting with a 6 and extending to the next 9
(every 6 will be followed by at least one 9). return 0 for no numbers.
"""


def summer_69(array):
    total = 0
    add = True
    for num in array:
        while add:
            if num != 6:
                total += num
                break
            add = False
        while not add:
            if num != 9:
                break
            add = True
            break
    return total


print(summer_69([1, 2, 3, 4, 5, 6, 7, 8, 9]))
