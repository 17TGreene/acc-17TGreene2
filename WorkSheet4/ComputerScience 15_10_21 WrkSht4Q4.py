number = -1
while number < 0:
    try:
        reply = int(input("Please enter a positive number."))
        if reply > 0:
            number = reply
        else:
            print("This number isnt positive.")
    except ValueError:
        print("This isnt a number.")
        pass
        
print(number,"is a positive number.")