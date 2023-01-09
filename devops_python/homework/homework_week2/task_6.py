print("Enter a string")
str1 = input()
print("Enter a starting number")
starting_number = int(input())
print("Enter an ending number")
ending_number = int(input())
converted = str1[(starting_number-1): ending_number]
print(converted)