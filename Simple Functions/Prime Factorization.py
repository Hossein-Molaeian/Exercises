"""
Prime Factorization:
Have the user enter a number and find all Prime Factors (if there are any) and display them.
"""


def find_primes(n):
    primes_upto = []

    for num in range(2, n+1):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            primes_upto.append(num)

    return primes_upto


def prime_factorization(n):
    prime_factors = []
    primes_upto = find_primes(n)

    while n != 1:

        for div_num in primes_upto:
            if n % div_num == 0:
                n //= div_num
                prime_factors.append(div_num)

    print(prime_factors)


prime_factorization(1092)
