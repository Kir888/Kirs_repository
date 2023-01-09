def fibonacci_seq(n):
    if n == 1 or n == 2:
        return 1
    elif n == 0:
        print("No Fibonacci number")
    else:
        f1 = 1
        f2 = 1
        for num in range(3,n+1):
            fn = f1 + f2
            f1 = f2
            f2 = fn
        print(f"your fibonacci number is {fn}")
fibonacci_seq(20)
            