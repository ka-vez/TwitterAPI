from django.test import TestCase

# Create your tests here.
def factorial(n: int):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
    

def fibonacci(n: int):
    if n < 1:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

fib8 = [
    fibonacci(0),
    fibonacci(1),
    fibonacci(2),
    fibonacci(3),
    fibonacci(4),
    fibonacci(5),
    fibonacci(6),
    fibonacci(7),
    fibonacci(8),
]

print(fib8)
