def collatz(n):  # NOT RECURSIVE
    steps = 0
    while n != 1:
        if not n % 2 == 0:
            n = n*3+1
        n /= 2
        steps += 1
    print(f"number of steps to get your number to 1 is: {steps}")


def collatz_recursive(n, steps=0):  # RECURSIVE
    if n <= 1:
        return steps
    if n % 2 == 0:
        return collatz_recursive(n/2, steps+1)
    else:
        return collatz_recursive(n*3+1, steps+1)


input_num = int(input("Enter a number bigger than 1: "))
if input_num <= 1:
    print("That is not bigger than 1.")
else:
    collatz(input_num)
