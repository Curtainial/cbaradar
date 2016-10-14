import random



def roll_one(n):
    r = random.random()
    result = int(r*n)+1
    return result


def roll_dice(d,n):
    already_rolled = 0
    total = 0
    while already_rolled < d:
        die = roll_one(n)
        total = total + die
        return total

i = 0
while i <20:
    print(roll_one(20))
    i = i+1




