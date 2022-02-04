L = [5, 7, 3, 6, 2, 4, 1]
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
                    myList[j],L[j+1] = myList[j+1],myList[j]
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
        
        


print(bubbleSort(L,True,True))

            
    
    