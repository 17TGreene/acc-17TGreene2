myNum = 19

def addUp(num):
    if num == 1:
        return 1
    else:
        return num+addUp(num-1)
print(addUp(myNum))