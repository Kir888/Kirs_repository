print("Enter a string")
str1 = input()
last_character = str1[-1]
first_character = str1[0]
first_character = first_character.replace("x","")
last_character = last_character.replace("x","")

middle_characters = str1[1:-1]

var = first_character + middle_characters + last_character

print(var)