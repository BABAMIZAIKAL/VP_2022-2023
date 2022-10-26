num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

binaryNumber = format(num1, 'b')
reversedBinaryNumber = binaryNumber[::-1]

print(reversedBinaryNumber[num2])

