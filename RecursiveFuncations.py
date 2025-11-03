# Program 11: Recursive Functions

# (a) Factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

num = int(input("Enter a number to find its factorial: "))
print("Factorial:", factorial(num))
print("--------------------------------")

# (b) nth Fibonacci number
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Enter position (n) for Fibonacci number: "))
print(f"Fibonacci({n}):", fibonacci(n))
print("--------------------------------")

# (c) Sum of a list
def sum_list(lst):
    if not lst:
        return 0
    return lst[0] + sum_list(lst[1:])

lst = list(map(int, input("Enter numbers in the list separated by spaces: ").split()))
print("Sum of List:", sum_list(lst))
print("--------------------------------")

# (d) Sum of first N whole numbers
def sum_n_numbers(n):
    if n == 0:
        return 0
    return n + sum_n_numbers(n - 1)

n = int(input("Enter a number to find sum of first N whole numbers: "))
print("Sum of first", n, "numbers:", sum_n_numbers(n))
print("--------------------------------")

# (e) Reverse a string
def reverse_string(s):
    if len(s) == 0:
        return s
    return reverse_string(s[1:]) + s[0]

s = input("Enter a string to reverse: ")
print("Reversed String:", reverse_string(s))
print("--------------------------------")
