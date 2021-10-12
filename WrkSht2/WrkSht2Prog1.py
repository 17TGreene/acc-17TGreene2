amount=int(input("How many numbers do you need to sort?"))
sortList=[]
for i in range(amount):
    sortInput = int(input("Enter an integer to be sorted."))
    sortList.append(sortInput)
sortList.sort(reverse = True)
print(sortList)
    