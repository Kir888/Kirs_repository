import sys
list = [102,5,6,78,54,43,76]
second_highest = -sys.maxsize -1
highest = -sys.maxsize -1
for a in list:
    if a > highest:
        second_highest = highest
        highest = a
    elif a > second_highest:
        second_highest = a
print(f"Highest number is {highest} and Second highest number is {second_highest}")
