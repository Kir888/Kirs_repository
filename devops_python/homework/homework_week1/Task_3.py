input = 66558

first_digit = input // 10000
second_digit = input % 10000 // 1000
third_digit = input % 1000 // 100
fourth_digit = input % 100 // 10
fifth_digit = input % 10

output = fifth_digit * 10000 + fourth_digit * 1000 + third_digit * 100 + second_digit * 10 + first_digit

print("The output is", output)