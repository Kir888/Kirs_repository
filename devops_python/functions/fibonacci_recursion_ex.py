#Print the fibonacci numbers till the given number.
#Fibonacci numbers are created by finding sum of previous 2 number.
#Fibonacci numbers start with two 1
# 1 - 1 - 2 - 3 - 5 - 8 - 13 - 21 - 34
def fibonacci_sequence(n):
    f1 = 1
    f2 = 1
    if n == 1 or n == 2:
        return 1
    elif n <0:
        print("No fibonacci number")
    else:
        for number in range (3,n+1):
           fn = f1 + f2
           f1 = f2
           f2 = fn
        return fn
fibonacci_sequence(10)

def fibonacci_rec(n):
    if n == 1 or n == 2:
        return 1
    elif n < 0:
        return "No fibonacci number"
    else:
        return fibonacci_rec(n-1) + fibonacci_rec(n-2)
number = int(input("Enter a fibonacci sequence number:"))
fibonacci_sequence_number = ""
for num1 in range(1,number +1):
    fibonacci_sequence_number = fibonacci_sequence_number + str(fibonacci_rec(num1)) + " - "
print(fibonacci_sequence_number.removesuffix(" - "))