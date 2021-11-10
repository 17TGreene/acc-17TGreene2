listNums = []
for i in range(5):
    listNums.append(int(input("Please input a number.")))
    
answer = 1    
for x in listNums:
    answer *= x
    
print(answer)