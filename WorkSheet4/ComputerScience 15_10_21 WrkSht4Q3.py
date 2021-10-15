number = input("Enter a number to be reversed.")
answer = ""
lengthCounter = len(number)
while lengthCounter > 0:
    answer += number[-1]
    number = number[0:len(number)-1]
    lengthCounter -=1
    
print(answer)
