def fib(n):    
    """Display the n first terms of Fibonacci sequence"""
    a, b = 0, 1
    for i in range(n):
        print(b)
        a, b = b, a+b

fib(10)

