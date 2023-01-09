# print("Enter a number")
# num1 = int(input())
# print("Enter a number")
# num2 = int(input())
# print("Enter a number")
# num3 = int(input())

sum = 0
for n in range(3):
    print("Enter a number")
    number = int(input())
    if number % 10 > 4:
       number = number - number % 10 + 10
    elif number % 10 <= 4:
       number = number - number % 10
    sum += number
print(sum)
  

