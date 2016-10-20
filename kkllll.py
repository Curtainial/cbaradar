#!/usr/bin/python3
#
# Assignment 3
# CMPS 5P, Fall 2016
#
# Cyrus Baradaran-Azimi
# cbaradar@ucsc.edu






import random

start = float((input("What is the starting number (1-499)? " )))
while start < 1 and start > 499:
    start = float((input("What is the starting number (1-499)? " )))
#these lines prevent the user from inputting anything other than the options provided
start_min = int(start-1)
start_max = int(start+1)


max = (input("What is the maximum value (" + str(start_max) + "-500)" + "? "))
while int(max) <= int(start) or int(max) > 500:
    max = int((input("What is the maximum value (" + str(start_max) + "-500)" + "? ")))
#these lines prevent the user from inputting anything other than the options provided

min = int((input("What is the minimum number (0-" + str(start_min) + ")?" )))
while int(min) >= int(start) or int(min) < 0:
    min = int((input("What is the minimum number (0-" + str(start_min) + ")?" )))
#these lines prevent the user from inputting anything other than the options provided


right_percent = int(input("What's the percentage chance of moving right (1-99)? "))
while int(right_percent) <= 0 or int(right_percent) >= 100:
    right_percent = int(input("What's the percentage chance of moving right (1-99)? "))
#these lines prevent the user from inputting anything other than the options provided


walks = int(input("How many walks (1-10000)? "))
while int(walks) <= 0 or int(walks) >= 10001:
    walks = int(input("How many walks (1-10000)? "))

#these lines prevent the user from inputting anything other than the options provided

fullwalks = []
maxwalks = []
minwalks = []
minstds = []
maxstds = []
allstds = []

#Arrays keep track of listings when they change

for x in range(walks):
    place = start
    steps = 0
#Sets the current location of the token to the starting position
    while steps != 5000 and place != min and place != max:
        right_prob = random.randint(1,100)
        if right_prob < right_percent:
            place +=1
#Makes it go right if lower than the percentage provided
        else:
            place -=1
        steps +=1
#Otherwise it goes left
    if steps == 5000:
            fullwalks.append(steps)
#Keeps track of how many times it reached 5k steps
    elif place == min:
            minwalks.append(steps)
#Keeps track of how many times it reached the min distance
    else:
         maxwalks.append(steps)
#Keep strack of how many times it reached the max distance


allwalks = minwalks + fullwalks + maxwalks
#Keeps track of total walks

print("WALKS THAT ENDED ON THE LEFT")
if len(minwalks) == 0:
    print("Number of walks: 0")
else:
    for x in range(len(minwalks)):
            meanmin = (sum(minwalks)/len(minwalks))
            minstds.append((minwalks[x] - sum(minwalks)/len(minwalks))** 2)
    minstdsans = ((sum(minstds)/len(minstds))** (1/2))
    print("Number of walks: " + str(len(minwalks)))
    print("Mean number of steps per walk: " + str(float((sum(minwalks)/len(minwalks)))))
    print("Standard deviation of number of steps per walk: " + str(minstdsans))
#These lines calculate the mean and standard deviation for all walks that hit the minimum
print("WALKS THAT ENDED ON THE RIGHT:")
if len(maxwalks) == 0:
    print("Number of walks: 0")
else:
    for x in range (len(maxwalks)):
        meanmax = (sum(maxwalks)/len(maxwalks))
        maxstds.append((maxwalks[x] - meanmax) ** 2)
    maxstdsans = ((sum(maxstds)/len(maxstds)) ** (1/2))

    print("Number of walks: " + str(len(maxwalks)))
    print("Mean number of steps per walk: " + str(meanmax))
    print("Standard deviation of number of steps per walk: " + str(maxstdsans))
#These lines calculate the mean and standard deviation for all walks that hit the maximum



print("WALKS THAT USED ALL 5000 STEPS:")
if len(fullwalks) == 0:
    print("Number of walks: 0")
else:
    print("Number of walks: " + str(len(fullwalks)))
    print("Mean number of steps: " + str(5000))
    print("Standard deviation of number of steps per walk: " + str(0))
#These lines calculate the mean and standard deviation for all walks that hit total number of steps


print("All walks:")
print("Number of walks: " + str(len(allwalks)))
print("Mean number of steps: " + str((sum(allwalks)/len(allwalks))))
for x in range(len(allwalks)):
        allstds.append((allwalks[x] - sum(allwalks)/len(allwalks)) ** 2)
allstdsans = ((sum(allstds)/len(allstds)) ** (1/2))
print("Standard deviation of number of steps per walk: " + str(allstdsans))
#These lines calculate the mean and standard deviation for all walks summed together.


#Standard deviation calculations found at http://standard-deviation.appspot.com/



