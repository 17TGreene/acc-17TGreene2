total = 0

file = open("Readme.txt","r")

line = file.readline()

while line:
    for i in line:
        if i.isalpha():
            i = i.lower()
            if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
                total+=1
    line = file.readline()
print("There are",total,"vowels in this file.")