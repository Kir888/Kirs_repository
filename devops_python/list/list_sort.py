list = [0,2,5,11,100,200,6,1]


for index in range(len(list)):
    for k in range(index+1,len(list)):
        if list[index] > list[k]:
            temp = list[index]
            list[index] = list[k]
            list[k] = temp
print(list)