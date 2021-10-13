firstTerm = int(input("Enter the number you want to form the multiplication table of."))
iterations = int(input("How long do you want the table to be?(Enter the number of sums needed.)"))
secondTerm = 1
while secondTerm <= iterations:
    print(firstTerm,"x",secondTerm,"=",firstTerm*secondTerm)
    secondTerm += 1
