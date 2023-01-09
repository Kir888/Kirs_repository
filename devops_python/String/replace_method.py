print("Enter any word")
str = input()
first_letter = str[0]
last_letter = str[-1]
middle = str[1:-1]
converted = first_letter + middle.replace("x","") + last_letter
print(converted)

n = 36

str = "Total nu" + n
print(str)