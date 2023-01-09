print("Enter a min number")
min = int(input())
print("Enter a max number")
max = int(input())
sum = 0
for n in range(min,max +1):
    if n % 11 == 0 and n % 3 == 0:
        sum += n
print (sum)