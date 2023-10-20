"""
Given 3 integers between 1 and 11, if their sum is less than or equal to 21,
return their sum, if their sum exceeds 21 and there's an eleven, reduce the total 
sum by 10. Finally, if the sum (even after adjustment) exceeds 21 return "BUST".
"""


def blackjack(a, b, c):
    sum = a+b+c
    if 1 <= a and b and c <= 11:
        if sum <= 21:
            return sum
        elif (sum) > 21 and 11 in (a, b, c):
            sum = sum-10
            if (sum) > 21:
                return "BUST"
