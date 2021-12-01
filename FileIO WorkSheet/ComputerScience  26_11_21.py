random10 = open("10Random.txt","r")
random100 = open("100random.txt","r")
filelist = [random10,random100]
resultlist=[]
writestring = ""
for file in filelist:
    list10 = []
    #convert to list
    for i in file:
        print(i, end = " ")
        list10.extend(i.split(" "))
        del list10[len(list10)-1]
    writestring += "\n"+str(list10)+"\n"
    #integer conversion
    for i in list10:
        list10[list10.index(i)] = int(i)
    
    #frequency and mode
    mode = 0
    for i in list10:
        print("Frequency of "+str(i)+":"+str(list10.count(i)))
        writestring+="\n Frequency of "+str(i)+":"+str(list10.count(i))
        if list10.count(i) > list10.count(mode):
            mode = i
    print("Mode:",mode)
    writestring += "\n Mode: "+str(mode)
    #mean
    mean = 0
    for i in list10:
        mean += i
    mean/=len(list10)
    print("Mean:",mean)
    writestring += "\n Mean: "+str(mean)
    #median
    list10.sort()
    if len(list10)//2 == 0: 
        median = list10[(len(list10)/2)-1]
    else:
        median = list10[len(list10)//2]+list10[(len(list10)//2)-1]
        median/=2
    print("Median:",median)
    writestring+= "\n Median:"+str(median)
    #range
    print("Range:", max(list10)-min(list10))
    writestring+="\n Range:"+ str(max(list10)-min(list10))
    print("*******************************************************")
    writestring+="\n*******************************************************\n"
    
    resultlist.append(writestring)
    writestring=""
    

random10.close()
random100.close()

random10 = open("10RandomResult.txt","w")
random100 = open("100randomResult.txt","w")
random10.write(resultlist[0])
random100.write(resultlist[1])
random10.close()
random100.close()

