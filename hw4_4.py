num = int(input("Number: "))

i = 0
sum = 0
while i < num:
    newNum = ((i + 1) * str(num))
    if (i + 1) == num:
        print(newNum, end="=")
    else: print(newNum, end="+")
    sum += int(newNum)
    i+=1
print(sum)