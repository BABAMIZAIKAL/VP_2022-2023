
num = int(input("Enter number:"))
while num < 0:
    num = int(input("Enter number:"))

num2 = num + 2
i = 0
n1, n2 = 0, 1
curNum = 0
print(n1)
print(n2)
while i < num: 
    curNum = n1 + n2
    n1 = n2
    n2 = curNum
    print(curNum)
    i += 1