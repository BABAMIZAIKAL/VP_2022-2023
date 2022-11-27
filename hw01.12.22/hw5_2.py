num = int(input("Enter count:"))

i = 0
dict = dict()

while i < num:
    key = input("key:")
    value = input("value:")
    dict[key] = value
    i += 1

m = int(input("M:"))
i = 0
list = list()
while i < m:
    val = input("value: ")
    if val in dict.keys():
        list.append(dict[val])
        dict.pop(val)
    else: 
        list.append(val)
    i += 1


print(dict)
print(list)