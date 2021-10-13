firstNum = int(input("Enter your first number to have its Greatest Common Factor with another value found."))
secondNum = int(input("Enter your second value to have its Greatest Common Factor with the first value found."))

remainder = int
while remainder != 0:
    mainResult = firstNum // secondNum
    remainder = firstNum % secondNum
    firstNum = secondNum
    secondNum = remainder
print(firstNum,"is the GCF.")
    
    
