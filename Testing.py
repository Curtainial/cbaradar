import random

d = float(input("How many dice? "))
n = float(input("How many sides on said dice? "))


def roll_one(n):
    r = random.randint()
    result = r*n
    return result


def roll_dice(d,n):
    already_rolled = 0
    total = 0
    while already_rolled < d:
        die = roll_one(n)
        total = total + die
        return total



