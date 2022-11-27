def input_nums(n):
    list = []
    for i in range(n):
        num = input("Enter element: ")
        if num.isnumeric():
            list.append(num)
    return list

def sum_list(lst):
    sum = 0
    for i in range((len(lst))):
        if is_number(lst[i]):
            sum += float(lst[i])
    return sum

def max_of_two(a, b):
    if is_number(a) and is_number(b):
        if float(a) >= float(b):
            return a
        else: return b
    if is_number(a):
        if is_number(b) == False:
            return a
    if is_number(b):
        if is_number(a) == False:
            return b
    return

def is_number(a):
    if type(a) == int or type(a) == float:
        return True
    elif type(a) == str:
        if a.isnumeric():
            return True
    try:
        float(a)
        return True
    except ValueError:
        print("", end="")
    return False

print(max_of_two(sum_list(input_nums(4)), sum_list(3)))
print(max_of_two(sum_list([4, "AA@", 3.12, "1"]), "9.2"))
