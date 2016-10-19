import random,sys
#location = 0
#step =random.randint(0, 1) # returns 0 or 1, each with prob. 1/2
#if step == 0:
#    step = -1
#    location = location + step
#print (location)


def randomwalk():
    start = float((input("What is the starting number (1-499)? " )))
    while start < 1:
        start = float((input("What is the starting number (1-499)? " )))
#Makes sure the start isnt below 1
    start_min = int(start-1)
    start_max = int(start+1)


    max = (input("What is the maximum value (" + str(start_max) + "-500)" + "? "))

    min = (input("What is the minimum number (0-" + str(start_min) + ")?" ))

    right_percent = int(input("What's percentage chance of moving right (1-99)? "))
    walks = int(input("How many walks (1-1000)? "))

    right_prob = random.randint(1,right_percent)
    answer = True

    end = 0

    while answer == True:

        right_go = random.random(0,1)
        right_move = right_go * right_percent
        if right_move <= 1:
            steps = -1
            end = end + steps
        else:
            steps = 1
            end = end + steps

        guess = random.uniform(start_min,start_max)

        if guess == 0:
            steps = 1
            end = end + steps


    print(end)

randomwalk()







