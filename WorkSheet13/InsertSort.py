L = [5, 7, 3, 6, 2, 4, 1]

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
print("Insertion Sort:",insertionSort(L,True))