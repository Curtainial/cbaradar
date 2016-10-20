import random,sys


start = float((input("What is the starting number (1-499)? " )))
while start < 1 and start > 499:
    start = float((input("What is the starting number (1-499)? " )))
#these lines prevent the user from inputting anything other than the options provided
start_min = int(start-1)
start_max = int(start+1)


max = (input("What is the maximum value (" + str(start_max) + "-500)" + "? "))
while int(max) <= int(start) or int(max) > 500:
    max = (input("What is the maximum value (" + str(start_max) + "-500)" + "? "))
#these lines prevent the user from inputting anything other than the options provided

min = (input("What is the minimum number (0-" + str(start_min) + ")?" ))
while int(min) >= int(start) or int(min) < 0:
    min = (input("What is the minimum number (0-" + str(start_min) + ")?" ))
#these lines prevent the user from inputting anything other than the options provided


right_percent = int(input("What's the percentage chance of moving right (1-99)? "))
while int(right_percent) <= 0 or int(right_percent) >= 100:
    right_percent = int(input("What's the percentage chance of moving right (1-99)? "))
#these lines prevent the user from inputting anything other than the options provided


walks = int(input("How many walks (1-10000)? "))
while int(walks) <= 0 or int(walks) >= 10001:
    walks = int(input("How many walks (1-1000)? "))
#these lines prevent the user from inputting anything other than the options provided
steps = 0
place = start + steps


#allows the following loops to run

def randomwalk():
    steps = 0
    place = start + steps

    fullwalks = 0

    while steps < 5000:
        rightwalks = 0
        leftwalks = 0
        right_prob = random.randint(1,100)

        if right_prob >= right_percent:
            place = steps - 1 + start
        elif right_prob <=  right_percent:

            place = steps + 1 + start
            return place
        elif steps == 5000:
            fullwalks +=1
            return fullwalks

        elif place == min:

            leftwalks +=1
            return leftwalks
        elif place == max:

            rightwalks +=1
            return rightwalks

    steps += 1
    return steps




while walks != 0:
    print(randomwalk())
    walks -=1







