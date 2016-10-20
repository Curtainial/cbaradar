import random,sys


start = float((input("What is the starting number (1-499)? " )))
while start < 1:
    start = float((input("What is the starting number (1-499)? " )))

start_min = int(start-1)
start_max = int(start+1)


max = (input("What is the maximum value (" + str(start_max) + "-500)" + "? "))
while int(max) <= int(start) or int(max) > 500:
    max = (input("What is the maximum value (" + str(start_max) + "-500)" + "? "))

min = (input("What is the minimum number (0-" + str(start_min) + ")?" ))
while int(min) >= int(start) or int(min) < 0:
    min = (input("What is the minimum number (0-" + str(start_min) + ")?" ))


right_percent = int(input("What's the percentage chance of moving right (1-99)? "))
while int(right_percent) <= 0 or int(right_percent) >= 100:
    right_percent = int(input("What's the percentage chance of moving right (1-99)? "))

walks = int(input("How many walks (1-1000)? "))
while int(walks) <= 0 or int(walks) >= 1001:
    walks = int(input("How many walks (1-1000)? "))

answer = True


def randomwalk():
    steps = 0


    while answer == True:
        place = 0
        while steps < 5000:

            steps = steps + 1


            if random.randint(1,100) >= right_percent:

                place = steps + 1
                return steps

            elif():

                place = steps - 1
                return steps

    if steps == 5000:
        fullwalks = 0
        answer == False
        return steps

    elif place == min:
        minwalks = 0
        answer == False
        return steps

    elif place == max:
        maxwalks = 0
        answer == False
        return steps





while walks != 0:
    print(randomwalk())
    walks = walks - 1

print("Number of walks ")








