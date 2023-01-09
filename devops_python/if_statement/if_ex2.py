print("enter a positive number")
number = int(input())

first_condition = number % 10 <= 2
second_condition = number % 10 >= 8

result = first_condition or second_condition
if(result):
    print("Your number is within 2 of a multiple 10 ")
else:
    print("Your number didn't match the expected requirement")