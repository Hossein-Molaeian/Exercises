"""
Write a function that computes the first 'n' fibonacci numbers.
"""


def fibonacci(n):
    a, b = 0, 1
    numbers = []
    for sequence in range(n):
        numbers.append(b)
        a, b = b, a+b
    return numbers


print(fibonacci(10))
