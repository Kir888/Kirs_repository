# Create a function that returns average of numbers from give list.
# When we are calcualting the average we shouldn't include
#largest and smallest element in the array.
#If the largest or smallest number duplicate just not use on copy

def avg(l):
    l.sort()
    sum = 0
    for index in range(1,len(l)-1):
        sum+=l[index]
    return  sum / (len(l) -2)
print(avg([12,7,9,3,6,7,3]))

