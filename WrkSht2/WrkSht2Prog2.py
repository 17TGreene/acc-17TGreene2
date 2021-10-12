age = ""
while type(age) != int:
    try:
        age= int(input("Please enter your age."))
        
    except ValueError :
        print("This isnt an integer, please try again.")
        pass
    
if age >= 18:
    print("Congratulations, you are eligible to vote.")
else:
    print("You are not permitted to vote yet.")

    
