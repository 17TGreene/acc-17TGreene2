string = input("Enter your string")
answer = 0
for i in string:
    if i.isdigit() == True:
        answer += int(i)
print(answer)