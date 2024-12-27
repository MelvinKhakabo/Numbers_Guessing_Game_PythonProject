#Numbers_Guessing_Game

import math
import random

#Taking Inputs
lower = int(input("Enter Lower bound: "))
upper = int(input("Enter Upper bound: "))

#Generating random number between the lower and upper
x = random.randint(lower, upper)
total_chances = math.ceil(math.log(upper - lower + 1, 2))

print(f"\n\tYou've only {total_chances} chances to guess the integer!\n")

count = 0
flag = False

#for calculation of minimum number of guesses depends upon range
while count < total_chances:
    count += 1

    #Taking guessing number as input
    guess = int(input("Guess a number: "))

    #Condition testing
    if x == guess:
        print(f"Congratulations you did it in {count} try!")
        flag = True
        break
    elif x > guess:
        print("You guessed too small!")
    else:
        print("You guessed too high!")

#If Guessing is more than required guesses, show this output
if not flag:
    print(f"\nThe number is {x}")
    print("\tBetter Luck Next time!")
