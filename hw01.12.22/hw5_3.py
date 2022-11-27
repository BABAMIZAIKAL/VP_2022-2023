def list_avg(lst, multiplier = 1):
    sum = 0
    count = 0
    if type(multiplier) != int:
        print("Error")
        return
        
    for i in range((len(lst))):
        if type(lst[i]) == int or type(lst[i]) == float:
            lst[i] *= multiplier
            sum += lst[i]
            count += 1
        elif type(lst[i]) == str:
            if lst[i].isnumeric():
                lst[i] = int(lst[i]) * multiplier
                sum += int(lst[i])
                count += 1
    if count != 0:
        return(sum / count)
    else:
        print("Error: Division by zero")
        return

    

print(list_avg(["4", 1.5, "@7$", 3.5, (1, "hi")]))
print(list_avg(['6', 3, 3.0], 2))
print(list_avg(['%$', {}]))
print(list_avg([]))
