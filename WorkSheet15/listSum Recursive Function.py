L = [1,2,5,3,4,6,7]

def listSum(myList):
    if  len(myList) == 1:
        return  myList[0]
    else:
        return myList[0] + listSum(myList[1:])

print(listSum(L))

        

    