"""
Simple: given an integer, return True if it is within 10 of either 100 or 200
"""


def almost_there(n):
    return 90 <= n <= 110 or 190 <= n <= 210
