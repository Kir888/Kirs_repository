print("Enter a word")
str1 = input()
first_two_characters = str1[:2]
last_two_characters = str1[-2:]
bl = first_two_characters == last_two_characters
print(bl)

bl1 = str1.endswith(first_two_characters)

print(bl1)