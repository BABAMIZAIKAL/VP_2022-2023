num = int(input("Enter count:"))

i = 0
list = list()
while i < num:
    n = int(input("Enter number:"))
    list.append(n)
    i+=1

nullOrOne = int(input("Enter 0 or 1:"))
while nullOrOne != 0 and nullOrOne != 1:
    nullOrOne = int(input("Enter 0 or 1:"))

i = 0
if nullOrOne == 0:
    while i < len(list):
        if i % 2 == 0:
            list[i] += 5
        i+=1
elif nullOrOne == 1:
    while i < len(list):
        if i % 2 == 1:
            list[i] += 10
        i+=1

print(list)