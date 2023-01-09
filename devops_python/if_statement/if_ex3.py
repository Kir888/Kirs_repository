print("Enter a number")
number1 = int(input())
print("Enter a second number")
number2 = int(input())

sum_of_nums = number1 + number2
if sum_of_nums < 10:
    print("Sum of these two numbers is 10")
elif sum_of_nums >= 10 and sum_of_nums <= 20:
    print("Sum of these two numbers is 20")
else:
    print(f"Sum of these two numbers is {sum_of_nums}")