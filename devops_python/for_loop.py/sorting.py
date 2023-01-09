list1 = [1,267,34,56,59,18,2,879]
for index in range(len(list1)):
    for m in range(index +1,len(list1)):
        if list1[index] > list1[m]:
            temp = list1[index]
            list1[index] = list1[m]
            list1[m] = temp
print(list1)

