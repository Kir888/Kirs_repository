l = [1,99,100,110,200,34,99,199]
highest = l[0]
second_highest = l[0]
for a in l:
    if a > highest:
        second_highest = highest
        highest = a
    elif a > second_highest:
        second_highest = a
print(highest)       
print(second_highest)