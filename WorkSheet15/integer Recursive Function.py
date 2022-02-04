integer = 1235467

def sumInt(myInt):
    if myInt < 10:
        return myInt
    else:
        return myInt%10 + sumInt(myInt//10)
                              
print(sumInt(integer))
        