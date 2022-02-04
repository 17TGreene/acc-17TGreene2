L = [5, 7, 3, 6, 2, 4, 1]
ascending = False
def bubbleSort(myList):
    exchange = True
    length = len(myList)
    i = 0
    while length > 0 and exchange == True:
        exchange = False
        exchanges = 0
        print("Before pass ",i+1,":",myList,)
        print("Comparisons:",length-i-1)
        for j in range(length-i-1):
            if ascending == True:
                if myList[j] > myList[j+1]:
                    myList[j],L[j+1] = myList[j+1],myList[j]
                    exchange = True
                    exchanges+=1
            else:
                if myList[j] < myList[j+1]:
                    myList[j],L[j+1] = myList[j+1],myList[j]
                    exchange = True
                    exchanges+=1
                    
        print("Exchanges:",exchanges)
        print("After pass ",i+1,":",myList,)
        i+=1
    print(myList)
bubbleSort(L)

            
    
    