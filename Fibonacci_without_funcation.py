# Program to print first n Fibonacci numbers

n = int(input("Enter how many Fibonacci numbers to display: "))

# First two Fibonacci numbers
a, b = 0, 1

if n <= 0:
    print("Please enter a positive number.")
elif n == 1:
    print("Fibonacci sequence:")
    print(a)
else:
    print("Fibonacci sequence:")
    print(a, b, end=" ")
    for i in range(2, n):
        c = a + b
        print(c, end=" ")
        a, b = b, c
