list = ["a","b","c","d"]
answers = ["1","2","3","4","5","6","7","8","9","10"]
running = True

while running == True:
    activeLoop = "Y"
    answer = ""
    userInput = ""
    answer = input("""1. Append an element
    2. Insert an element
    3. Append a list to the given list
    4. Modify an existing element
    5. Delete an existing element from its position
    6. Delete an existing element with a given value
    7. Sort the list in the ascending order
    8. Sort the list in descending order
    9. Display the list.
    10. Exit the application.
    Please enter your choice (1-10):""")
    print("""
****************************************************
""")
    if answers.count(answer) == 0:
        print("That isnt an option, enter a a number from 1-10.")
    else:
        while activeLoop == "Y":
            if answer == "1":
                userInput = ""
                userInput = input("Enter a value to append to the list:")
                print(list)
                list.append(userInput)
                print(list)
                
                       
                   
                
            elif answer == "2":
                userPos = ""
                print(list)
                userInput = input("Enter a value to be inserted:")
                while type(userPos) != int:    
                    try:
                        userPos = int(input("Enter its position in the list:"))
                    except ValueError:
                        print("Please input and integer.")
                        pass
                
                list.insert(int(userPos),userInput)
                print(list)
           
            elif answer == "3":
                print(list)
                userInput = input("Insert a list to be appended to the main list, separated by commas:")
                userList = []
                lastComma = -1
                for i in range(len(userInput)):
                    if userInput[i] == ",":
                        userList.append(userInput[lastComma+1:i])
                        lastComma = i
                    
                userList.append(userInput[lastComma+1:])
                list.extend(userList)
                print(list)
                    
              
            elif answer == "4":
                print(list)
                userInput = input("Enter the a value to replace another value in the list:")
                userPos = ""
                while type(userPos) != int:
                    try:
                        userPos = int(input("Enter the position of the value to be modified in the list(starting from 0):"))
                    except ValueError:
                        print("This must be an integer.")
                list[userPos]=userInput
                print(list)
                
            
            elif answer == "5":
                print(list)
                userInput = ""
                while type(userInput) != int:
                    try:
                        userInput = int(input("Enter the position of the value to be deleted(starting from 0):"))
                    except ValueError:
                        print("This isnt an integer, try again.")
                    
                try:
                    del list[userInput]
                except IndexError:
                        print("There is not a value in this position.")
                print(list)
                
            
            elif answer == "6":
                print(list)
                userInput = input("Enter a value to be removed from the list:")
                try:
                    list.remove(userInput)
                except ValueError:
                    print("This value is not in the list.")
                print(list)
                
            
            elif answer == "7":
                print(list)
                list.sort()
                print(list)
                
            
            elif answer == "8":
                print(list)
                list.sort(reverse = True)
                print(list)
                
            elif answer == "9":
                print(list)
                
            elif answer == "10":
                exit()
       
            activeLoop = input("Would you like to repeat this operation?(Y/N)")    
            while activeLoop != "Y" and activeLoop !="N":
                activeLoop = input("Would you like to repeat this operation?(Y/N)")
            print("""
    ****************************************************
    """)
        
