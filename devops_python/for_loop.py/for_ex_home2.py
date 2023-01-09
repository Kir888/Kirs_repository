list = [54,67,12,15,623,525,329]
for index in range(len(list)):
    for a in range(index,len(list)):
        if list[index] > list[a]:
            temp = list[a]
            list[a] = list[index]
            list[index] = temp
print(list)