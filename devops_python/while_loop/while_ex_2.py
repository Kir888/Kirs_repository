#Prime numbers can be divided by 1 or itself

print("Enter a starting point")
starting_num = int(input())
print("Enter ending point")
ending_num = int(input())

while starting_num <= ending_num:
    possibe_divider = 2
    is_prime = True
    while possibe_divider < starting_num:
        if starting_num % possibe_divider == 0:
            is_prime = False
        possibe_divider += 1
    if is_prime and starting_num > 1:
        print(f"{starting_num} is a prime number")
    starting_num += 1
        