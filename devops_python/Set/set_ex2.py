import sys
s = [1,8,3,8,5,7]
s2 = {10,12,100,4,5}
lowest = sys.maxsize
second_lowest = sys.maxsize
for element in s:
    if element < lowest:      
        second_lowest = lowest
        lowest = element 
    elif element < second_lowest:
        second_lowest = element
print(second_lowest)

