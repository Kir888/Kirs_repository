row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
number = int(input("Enter a number "))
column = number // 10
row = number % 10
map[column-1][row-1] = "X"
print(f"{row1}\n{row2}\n{row3}")
