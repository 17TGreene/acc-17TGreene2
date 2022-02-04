import sys
try:
    if str(sys.argv[1]) == "--help":
        print("""Arguement 1: Ascending(True/False)
Arguement 2: Input(.txt file)
Arguement 3: Output(.txt file)
Arguement 3: Bubble/Insertion/Selection Sort(1/2/3)""")
        exit()
    else:
        sysAscending=bool(sys.argv[1])
        sysInput = str(sys.argv[2])
        sysOutput = str(sys.argv[3])
        sysRoutine = int(sys.argv[4])
except IndexError:
    sysAscending = True
    sysInput = ""
    sysOutput = "log.txt"
    sysRoutine = 3

if sysInput != "":
    L=[]
    inputFile = open(sysInput,"r")
    for i in inputFile:
        for j in (i.split(" ")):
            if j != "\n" and j != " ":
                L.append(int(j))
             
else:              
    L = [5, 7, 3, 6, 2, 4, 1]
def bubbleSort(myList,ascending = True):
    if str(sysOutput) != "":
        log = open(sysOutput,"w")
    exchange = True
    length = len(myList)
    i = 0
    while length > 0 and exchange == True:
        exchange = False
        exchanges = 0
        print("Before pass ",i+1,":",myList,)
        print("Comparisons:",length-i-1)
        if str(sysOutput) != "":
            log.write("\nBefore pass "+str(i+1)+": "+str(myList))
            log.write("\nComparisons:"+str(length-i-1))
            log.write("\nExchanges made:")
        for j in range(length-i-1):
            if ascending == True:
                if myList[j] > myList[j+1]:
                    myList[j],L[j+1] = myList[j+1],myList[j]
                    exchange = True
                    exchanges+=1
                    if str(sysOutput) != "":
                        log.write("\n"+str(myList)+": ("+ str(myList[j]) + " and "+ str(myList[j+1])+")")
            else:
                if myList[j] < myList[j+1]:
                    myList[j],myList[j+1] = myList[j+1],myList[j]
                    exchange = True
                    exchanges+=1
                    if str(sysOutput) != "":
                        log.write("\n"+str(myList)+": ("+ str(myList[j]) + " and "+ str(myList[j+1])+")")
                    
            
                    
        print("Exchanges:",exchanges)
        print("After pass ",i+1,":",myList,)
        if str(sysOutput) != "":
            log.write("\nTotal Exchanges: "+str(exchanges))
            log.write("\nAfter pass "+str(i+1)+": "+str(myList)+"\n")
        i+=1
    return(myList)
    if str(sysOutput) != "":
        log.close()
        
        
def insertionSort(sortList,ascending = True):
    marker = 1
    if str(sysOutput) != "":
        log = open(sysOutput,"w")
    while marker < len(sortList):
        ohHiMark = marker
        if ascending == True:
            while sortList[ohHiMark]<sortList[ohHiMark-1] and ohHiMark > 0:
                sortList[ohHiMark],sortList[ohHiMark-1]=sortList[ohHiMark-1],sortList[ohHiMark]
                ohHiMark -=1
                if str(sysOutput) != "":
                    log.write("Swapped "+str(sortList[ohHiMark])+" and "+str(sortList[ohHiMark+1])+"\n")
        else:
            while sortList[ohHiMark]>sortList[ohHiMark-1] and ohHiMark > 0:
                sortList[ohHiMark],sortList[ohHiMark-1]=sortList[ohHiMark-1],sortList[ohHiMark]
                ohHiMark -=1
                if str(sysOutput) != "":
                    log.write("Swapped "+str(sortList[ohHiMark])+" and "+str(sortList[ohHiMark+1])+"\n")
        if str(sysOutput) != "":
                    log.write("After loop "+str(marker)+":"+str(sortList)+"\n")
        marker+=1
        
    return sortList
    if str(sysOutput) != "":
        log.write(sortList)
        log.close

def selectionSort(aList,ascending):
    marker = 0
    if str(sysOutput) != "":
        log = open(sysOutput,"w")
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
        if str(sysOutput) != "":
            log.write("Swapped "+str(aList[minIndex])+" and "+str(aList[marker])+". Marker: "+str(marker)+"\n")
            log.write("List: "+str(aList)+"\n")
        marker+=1
    return aList
    if str(sysOutput) != "":
        log.write(aList)
        log.close




if sysRoutine == 1:
    print("Bubble Sort:",bubbleSort(L,sysAscending))
elif sysRoutine == 2:
    print("Insertion Sort:",insertionSort(L,sysAscending))
else:
    print("Selection Sort:",selectionSort(L,sysAscending))


            
    
    