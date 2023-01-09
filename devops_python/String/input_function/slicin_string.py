print("enter a string")
str1 = input()
two_first_letters = str1[0:2]

rest_of_word = str1[2:]

changed_word = rest_of_word + two_first_letters

print(changed_word)
