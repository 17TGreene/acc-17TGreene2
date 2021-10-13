itemNumber = 0
total = 0
numbersToAverage = int(input("How many numbers would you like to get the average of?"))
while itemNumber < numbersToAverage:
    total += int(input("Please enter a number."))
    itemNumber+=1
average = total/numbersToAverage
print("The average of your numbers is " + str(average) + ".")
    