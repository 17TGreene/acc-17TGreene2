string = input("Enter a string seperated by hyphens.")
last_hyphen = 0
for i in range(len(string)):
    if string[i] =="-":
        if last_hyphen == 0:
            print(string[:i])
        else:
            print(string[last_hyphen+1:i])
        last_hyphen = i
print(string[last_hyphen+1:])

    
        