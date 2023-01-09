print("Please enter three ingredients with spaces")
str1 = input()
print("Please enter the int number")
number = int(input())
first_letter1 = str1[0]
first_letter2 = str1[str1.find(" ") + 1]
first_letter3 = str1[str1.rfind(" ") + 1]
other_letters1 = str1[1:str1.find(" ")]
other_letters2 = str1[str1.find(" ") + 2:str1.rfind(" ")]
other_letters3 = str1[str1.rfind(" ") + 2:]
converged = str(number) + other_letters1 + " " + str(number + 1) + other_letters2 + " " + str(number +2) + other_letters3
print(converged)
