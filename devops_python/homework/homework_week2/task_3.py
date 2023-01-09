print("Enter a sentence with three words")
str = input()
last_index1 = str.find(" ") - 1
last_index2 = str.rfind(" ") - 1
last_index3 = len(str) - 1
sum = last_index1 + last_index2 + last_index3
print(
f"""{last_index1}
{last_index2} 
{last_index3} 
The sum: {sum}""")