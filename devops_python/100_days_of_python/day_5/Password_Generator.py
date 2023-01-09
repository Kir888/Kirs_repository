import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
print("Welcome to the PyPassword Generator!")
nr_letters = int(input(f"How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

str_letters= ""
for letter in range(nr_letters):
    random_digit_l = random.randint(0, len(letters)-1)
    random_letter = letters[random_digit_l]
    str_letters = str_letters + random_letter

str_symbols= ""
for symbol in range(nr_symbols):
    random_digit_s = random.randint(0, len(symbols)-1)
    random_symbol = symbols[random_digit_s]
    str_symbols = str_symbols + random_symbol

str_numbers= ""
for number in range(nr_numbers):
    random_digit_n = random.randint(0, len(numbers)-1)
    random_number = numbers[random_digit_n]
    str_numbers = str_numbers + random_number
password = str_numbers + str_symbols + str_letters
print(password)
randomized_password =""

nums = list(range(0,len(password)))
random.shuffle(nums)

for n in nums:
    randomized_password += password[n]
print(randomized_password)