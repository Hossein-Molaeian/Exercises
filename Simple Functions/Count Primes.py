"""
Hard: write a function that returns the number of prime numbers that
exist upto and including a given number(0 and 1 aren't prime)
"""


def count_primes(num):
    primes = [2]
    x = 3
    if num < 2:
        return 0
    while x <= num:
        for y in primes:
            if x % y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    return primes
