L = [0,4,2,8,5,3,1]
marker = 0

while marker < len(L):
    minIndex = marker
    for j in range(marker+1,len(L)):
        if L[minIndex]>L[j]:
            minIndex = j
        
    L[minIndex],L[marker]=L[marker],L[minIndex]
    marker+=1
               
        
                
print(L)