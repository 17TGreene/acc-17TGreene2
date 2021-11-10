length = int(input("How many rows?"))
for i in range(length+1):
    for x in range(i):
        print("*",end=" ")
    print()