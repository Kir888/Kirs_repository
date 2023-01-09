print("enter a password")
password = input()
lower = password.lower()
upper = password.upper()
is_there_lower = password != upper
is_there_upper = password != lower
is_valid = is_there_lower and is_there_upper
print(is_valid)