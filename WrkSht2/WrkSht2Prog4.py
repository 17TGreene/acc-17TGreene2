num = int(input("Please enter a number to be divided."))
if num % 7 == 0:
    print("This number is divisible by 7.", num//7)
else:
    print("This number is not divisble be 7.",num//7,"remainder",num%7)