num = int(input("Enter a number and we will check if its last digit is divisible by 3 or not."))
num = num%10
if num%3 == 0:
    print("The last digit of this number is divisble by 3.")
else:
    print("The last digit of this number is not divisble by 3.")