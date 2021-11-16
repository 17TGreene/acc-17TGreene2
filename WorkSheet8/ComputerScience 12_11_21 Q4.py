string = input("Enter a string")
counter = 0
vowels = 0
while counter < len(string):
    ch = string[counter]
    if(ch =="a" or ch=="e" or ch == "i" or ch == "o" or ch == "u"):
        print(ch)
        vowels += 1
    counter +=1
print(len(string)-vowels,"consonants.")