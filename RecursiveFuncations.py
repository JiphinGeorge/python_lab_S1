# Program 11: Recursive Functions

# (a) Factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# (b) nth Fibonacci number
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# (c) Sum of a list
def sum_list(lst):
    if not lst:
        return 0
    return lst[0] + sum_list(lst[1:])

# (d) Sum of first N whole numbers
def sum_n_numbers(n):
    if n == 0:
        return 0
    return n + sum_n_numbers(n - 1)

# (e) Reverse a string
def reverse_string(s):
    if len(s) == 0:
        return s
    return reverse_string(s[1:]) + s[0]

# Examples
print("Factorial:", factorial(5))
print("Fibonacci(7):", fibonacci(7))
print("Sum of List:", sum_list([1, 2, 3, 4, 5]))
print("Sum of first 10 numbers:", sum_n_numbers(10))
print("Reversed String:", reverse_string("HELLO"))
