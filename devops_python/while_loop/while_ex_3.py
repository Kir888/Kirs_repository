print("enter a string")
str = input()


index = 0
is_duplicated = False
while index < len(str):
    print(str[index])
    if str.count(str[index]) > 1:
        is_duplicated = True
    index += 1
if is_duplicated:
    print((str), "contains duplicated letters")
elif not is_duplicated:
    print(f"{str} doesn't contain any duplicated letters")