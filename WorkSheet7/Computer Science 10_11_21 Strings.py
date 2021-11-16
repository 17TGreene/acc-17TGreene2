string = "Hello There Bob"

print(len(string))
print(string[0])
print(string[4])
print(string[len(string)-1])

for ch in string:
    print(ch)

for ch in range(0,len(string)):
    print(string[ch])
    
for ch in range(0, len(string)):
    print(ch)
    
print(string.upper())
print(string.lower())
print(string.count("l"))
print(string.find("b"))
print(string.replace("l","w"))
print(string.islower())
print(string.isupper())
print(string.isalnum())
print(string.isalpha())
print(string.isdigit())
print(string.index("o"))
print(string.strip())

string[0] = "W"
#Strings are immutable, us replace() to change characters
