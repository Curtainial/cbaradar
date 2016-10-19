import random

#location = 0
#step =random.randint(0, 1) # returns 0 or 1, each with prob. 1/2
#if step == 0:
#    step = -1
#    location = location + step
#print (location)


def randomwalk():
    start = float((input("What is the starting number (1-499)? " )))
    start_min = int(start-1)
    start_max = int(start+1)
    min = (input("What is the minimum number (0-" + str(start_min) + ")?" ))
    max = (input("What is the maximum value (" + str(start_max) + "-500)" + "? "))
    right_percent = int(input("What's percentage chance of moving right (1-99)? "))
    walks = int(input("How many walks (1-1000)? "))

randomwalk()



