str1 = input("""enter a string
""")
reversed_string = ""
for index in range(len(str1)):
    reversed_string += (str1[(index+1)*-1]) 
reversed_string = reversed_string.strip(" ")
print(reversed_string)

