print("Enter a word")
str1 = input()

print("Enter a second word")
str2 = input()

last_two = str1[-2:]

condition1 = str2.startswith(last_two)

first_two = str2[:2]
condition2 = str1.startswith(first_two)

print(condition1 or condition2)