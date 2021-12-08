def findmax(n1,n2):
    if n1>n2:
        print(n1)
    elif n1>n2:
        print(n1,"=",n2)
    else:
        print(n2)
def findProduct(n1,n2):
    print(n1*n2)
def findStringBackwards(string1):
    answer = ""
    for i in string1:
        answer = i+answer
    print(answer)
def evenList(list1):
    for i in list1:
        if i%2 == 0:
            print(i)
            
def findmaxNoArgs():
    if num1>num2:
        print(num1)
    elif num1>num2:
        print(num1,"=",num2)
    else:
        print(num2)
def findProductNoArgs():
    print(num1*num2)
def findStringBackwardsNoArgs():
    answer = ""
    for i in stringinput:
        answer = i+answer
    print(answer)
def evenListNoArgs():
    for i in listinput:
        if i%2 == 0:
            print(i)
            
            
            
            
            
            
num1 = int(input("Enter the first number."))
num2 = int(input("Enter the second number."))
stringinput = input("Enter a string")
listinput = [1,2,3,4,5,6]

findmax(num1,num2)
print("*********")
findProduct(num1,num2)
print("*********")
findStringBackwards(stringinput)
print("*********")
evenList(listinput)
print("*********")
print("*********")
findmaxNoArgs()
print("*********")
findProductNoArgs()
print("*********")
findStringBackwardsNoArgs()
print("*********")
evenListNoArgs()
print("*********")
