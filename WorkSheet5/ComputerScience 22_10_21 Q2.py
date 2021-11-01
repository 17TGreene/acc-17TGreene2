cardNum = ""
while type(cardNum) == str or len(str(cardNum)) > 16 or len(str(cardNum)) <= 13:
    try:
        cardNum = int(input("Please enter a valid credit card number. This number must be between 13 and 16 digits and contain no letters or decimals."))
    except ValueError:
        pass
cardNum = str(cardNum)
if cardNum[:1] == "4":
    print("This is a Visa card.")
elif cardNum[:1] == "5":
    print("This is a Master card")
elif cardNum[:2] == "37":
    print("This is an American Express card.")
elif cardNum[:1] == "6":
    print("This is a Discover card.")
else:
    print("This not a valid number.")
    exit()
    
counter = len(cardNum)-2
evens = 0
while counter >= 0:
    evenNo = int(cardNum[counter])*2
    if len(str(evenNo)) > 1:
        evenNo = int(str(evenNo)[0]) + int(str(evenNo)[1])
    evens += evenNo
    counter -=2

counter = len(cardNum)-1
odds = 0
while counter >= 0:
    odds += int(cardNum[counter])
    counter -=2
    

if (evens + odds) % 10 == 0:
    print("This card is valid.")
else:
    print("This card is not valid.")


#4388576018402626
#0123456789012345
#1234567890123456
#379354508162306