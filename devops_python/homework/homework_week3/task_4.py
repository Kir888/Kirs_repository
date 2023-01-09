print("Enter a number between 1 to 10")
num = int(input())
for n in range(1,num+1):
    str1 = str(num) * num
    num -= 1
    print(str1)
