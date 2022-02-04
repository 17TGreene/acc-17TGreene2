
def bubbleSort(myList,ascending = True,debug = False):
    if debug == True:
        log = open("log.txt","w")
    exchange = True
    length = len(myList)
    i = 0
    while length > 0 and exchange == True:
        exchange = False
        exchanges = 0
        print("Before pass ",i+1,":",myList,)
        print("Comparisons:",length-i-1)
        if debug == True:
            log.write("\nBefore pass "+str(i+1)+": "+str(myList))
            log.write("\nComparisons:"+str(length-i-1))
            log.write("\nExchanges made:")
        for j in range(length-i-1):
            if ascending == True:
                if myList[j] > myList[j+1]:
                    myList[j],myList[j+1] = myList[j+1],myList[j]
                    exchange = True
                    exchanges+=1
                    if debug == True:
                        log.write("\n"+str(myList)+": ("+ str(myList[j]) + " and "+ str(myList[j+1])+")")
            else:
                if myList[j] < myList[j+1]:
                    myList[j],myList[j+1] = myList[j+1],myList[j]
                    exchange = True
                    exchanges+=1
                    if debug == True:
                        log.write("\n"+str(myList)+": ("+ str(myList[j]) + " and "+ str(myList[j+1])+")")
                    
            
                    
        print("Exchanges:",exchanges)
        print("After pass ",i+1,":",myList,)
        if debug:
            log.write("\nTotal Exchanges: "+str(exchanges))
            log.write("\nAfter pass "+str(i+1)+": "+str(myList)+"\n")
        i+=1
    return(myList)
    if debug == True:
        log.close()
        
        
def insertionSort(sortList,ascending = True):
    marker = 1
    while marker < len(sortList):
        ohHiMark = marker
        if ascending == True:
            while sortList[ohHiMark]<sortList[ohHiMark-1] and ohHiMark > 0:
                sortList[ohHiMark],sortList[ohHiMark-1]=sortList[ohHiMark-1],sortList[ohHiMark]
                ohHiMark -=1
        else:
            while sortList[ohHiMark]>sortList[ohHiMark-1] and ohHiMark > 0:
                sortList[ohHiMark],sortList[ohHiMark-1]=sortList[ohHiMark-1],sortList[ohHiMark]
                ohHiMark -=1
        marker+=1
    return sortList

def selectionSort(aList,ascending):
    marker = 0
    while marker < len(aList):
        minIndex = marker
        for j in range(marker+1,len(aList)):
            if ascending == True:
                if aList[minIndex]>aList[j]:
                    minIndex = j
            else:
                if aList[minIndex]<aList[j]:
                    minIndex = j
        aList[minIndex],aList[marker]=aList[marker],aList[minIndex]
        marker+=1
    return aList


method = input("""Welcome to the sorter. Please choose a sorting method.
***********************************************************************
Enter 1 to use a Bubble Sort. Enter 2 to use an Insertion Sort.Enter 3 to use a Simple Selection Sort.""")

upOrDown = input("""Should the list be sorted in ascending or descending order?
***********************************************************************
Enter 1 for ascending. Enter any other input for descending.""")

inputList = input("Enter your list,seperated by commas.")
inputList = inputList.split(",")
for i in range(len(inputList)):
    inputList[i] = int(inputList[i])
    
if upOrDown == "1":
    upOrDown = True
else:
    upOrDown == False

if method == "1":
    print(bubbleSort(inputList,upOrDown))
elif method == "2":
    print(insertionSort(inputList,upOrDown))
elif method == "3":
    print(selectionSort(inputList,upOrDown))
else:
    print("Invalid method. Restart to retry.")