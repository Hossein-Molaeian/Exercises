import random


def coin_flip():

    heads, tails = 0, 0
    times = int(input("How many times do you want to flip the coin? "))
    for _ in range(times):
        coin_side = random.randint(0, 1)
        if coin_side == 0:
            heads += 1
        elif coin_side == 1:
            tails += 1

    print(f"Times tails appeared: {tails}\nTimes heads appeared: {heads}")


coin_flip()
