decimalValue = int(input("Please enter a decimal value to be converted to binary."))
binaryAnswer = ""
while decimalValue != 0:
    binaryAnswer = str(decimalValue % 2) + binaryAnswer
    decimalValue //= 2
print("Binary:",binaryAnswer)
    