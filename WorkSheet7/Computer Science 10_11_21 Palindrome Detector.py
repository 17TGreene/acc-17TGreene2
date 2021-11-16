string = input("Enter a palindrome")
string = string.upper()
for ch in range(len(string)):
    if string[ch] == string[(len(string)-1)-ch]:
       palindrome = True
    else:
        palindrome = False
if palindrome == False:
    print("This isn't a palindrome.")
else:
    print("This is a palindrome.")