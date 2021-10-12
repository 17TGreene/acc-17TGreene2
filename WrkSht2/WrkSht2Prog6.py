unitsTotal = int(input("Please enter the amount of units you have consumed."))
if unitsTotal >= 200:
    bill = 500 + ((unitsTotal-200)*10)
    print("Your bill is ",bill,"cents.")
elif unitsTotal <= 100:
    print("Congratulations, your bill is free!")
elif unitsTotal > 100:
    bill = (unitsTotal - 100) * 5
    print("Your bill is ", bill,"cents.")

    
    