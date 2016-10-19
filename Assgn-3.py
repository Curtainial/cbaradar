import random,sys


#location = 0
#step =random.randint(0, 1) # returns 0 or 1, each with prob. 1/2
#if step == 0:
#    step = -1
#    location = location + step
#print (location)






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



end = 0

answer = True


def randomwalk():




    while answer == True:


        if random.randint(1,99) <= right_percent:

            steps = 1
            end = start + steps
            return end

        else:

            steps = -1
            end = start + steps
            return end


        max_steps = 0
        min_steps = 0

        if end == start_max:
            max_steps +=1
            return max_steps

        if end == start_min:
            min_steps +=1
            return min_steps



while walks != 0:
    print(randomwalk())
    walks = walks - 1










