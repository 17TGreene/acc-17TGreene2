num = input("Input a number to recieve the sum of its digits.")
length = int(len(num))
answer = 0
while length > 0:
    answer += int(num[(length-1)])
    length -=1

print(answer)