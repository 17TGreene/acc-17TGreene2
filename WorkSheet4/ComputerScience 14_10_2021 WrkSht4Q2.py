num = 100
while num <= 500:
    first = num %10
    second = ((num - first)%100)/10
    third = (num - (num%100))/100
    if (first**3) + (second**3) + (third**3) == num:
        print(num)
    num += 1
    
