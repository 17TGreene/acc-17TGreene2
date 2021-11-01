import math
import random
lower = ""
upper = "" 
print("Enter 2 numbers to generate a random number between them(inclusive).")

while type(lower) == str or type(upper) == str:
    try:
        lower = int(input("Please enter a number."))
        upper = int(input("Please enter another number."))

    except ValueError:
        print("This input isnt an integer.")
        pass
    
if lower > upper:
    old = upper
    upper = lower
    lower = old
    
randomInt = random.randint(lower,upper)

minNumberGuesses = (round(math.log(upper-lower+1,2)))
#The -1 accounts for the first guess.
print("You have",minNumberGuesses,"guesses.")
answer = input("Guess the number the system generated.Enter your guess now.")
minNumberGuesses -= 1
while answer != str(randomInt) and minNumberGuesses > 0:
    if answer > str(randomInt):
        answer = input("Too high, guess again.")
    elif answer < str(randomInt):
        answer = input("Too low,guess again.")
    minNumberGuesses -=1

if answer == str(randomInt):
    print("Correct, your number was " + str(randomInt) + ".")
else:
    print("Oh well, your out of guesses. Try again next time.")
    