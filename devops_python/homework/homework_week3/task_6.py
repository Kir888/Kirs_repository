print("enter a sentence")
str1 = input()
completed_string = ""
for n in str1:
    if n.isupper():
        completed_string += " "
    completed_string += n
completed_string = completed_string.strip(" ")
print(completed_string)