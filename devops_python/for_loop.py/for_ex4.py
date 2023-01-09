list = [23,2,5,11,100,200,6,1]
# for a in list:
#     for b in list:
#         while a > b:
#             list = [a<b]
# print(list)

for index in range(len(list)):
    #list[index]
    for k in range(index+1,len(list)):
        if list[index] > list[k]:
            temp = list[index]
            list[index] = list[k]
            list[k] = temp
print(list)