print("Enter a string")
str1 = input()
print("Enter a string")
str2 = input()

if len(str1) == len(str2): 
    print(str1 + str2)
if len(str1) > len(str2):
    last_characters_str1 = len(str2)
    last_part_str1 = str1[-1*(last_characters_str1):]
    print(last_part_str1 + str2)
if len(str1) < len(str2):
    last_characters_str2 = len(str1)   
    last_part_str2 = str2[-1*(last_characters_str2):]
    print(str1 + last_part_str2)