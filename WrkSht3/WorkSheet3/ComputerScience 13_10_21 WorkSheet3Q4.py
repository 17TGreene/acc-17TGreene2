num=""
while type(num)!= int:
    try:
        num = int(input("Enter a number to find its factorial."))
    except ValueError:
        print("This isnt an integer. Please try again.")
        pass

multiplyBy = 1
total = 1
while multiplyBy <= num:
    total = total * multiplyBy
    multiplyBy += 1
    
print(total,"is the factorial of",num)
    