#!/usr/bin/python3
#
# Assignment 2
# CMPS 5P, Fall 2016
#
# Cyrus Baradaran-Azimi
# cbaradar@ucsc.edu





import random,sys

y = int(input("What is the maximum number? "))


#checking

b = y
a = 1
# a and b are bounds set for random integers. I used random.randint to find random numbers within these bounds.
initial_guess = y//2
#The initial guess is half the total value, creating a new range.




answeer = True


choose = initial_guess
#This gets the entire loop going. Once I set it, it gets changed after the first time, creating new barriers with it
while answeer == True:

    answer = input("Is your number greater than,[l]ess than, or [e]qual to " + str(choose) + "? ")

    if answer == "g":
        a = choose+1
        choose = random.randint(a,b)
#These lines create new boundaries for randomized numbers to get chosen from, with the lower bound as the guessed number + 1

    elif answer == "l":
        b = choose-1
        choose = random.randint(a,b)
#These lines create new boundaries for randomized numbers to get chosen from, with the upper bound the guess number - 1

    elif answer == "e":
        print("Hooray! I knew it! your answer was " + str(choose) + "! ")
        answer != True
        sys.exit()
#These lines display a victory message when the number is correct, and then ends the program.
