# 2. Write a function that returns true if sum of any two elements of an array results in sum
# Example
# Input : [1,10,3,7,8], 15 
# Output: false
def sum_of_elements():
    numbers = list(input("Type numbers with coma "))
    sum = int(input("Type sum "))
    for n in numbers:
       for m in (range(1, len(numbers))):
            if n + numbers[m] == sum:
                bool1 = True    
    print(bool1)
sum_of_elements()