# ------------------------------------------------------------
# 1. Accept full name and display in reverse order with space
# ------------------------------------------------------------

def reverse_full_name(name):
    words = name.split()                  # Split name into words
    reversed_words = words[::-1]          # Reverse the word order
    return " ".join(reversed_words)       # Join them with spaces

# Example:
print("Q1:", reverse_full_name("Jiphin George"))  # Output: George Jiphin


# ------------------------------------------------------------
# 2. Accept a list of single-digit numbers as input string and concatenate
# ------------------------------------------------------------

def concatenate_digits(digit_list):
    return int("".join(map(str, digit_list)))  # Convert list elements to string and join

# Example:
print("Q2:", concatenate_digits([1, 2, 3, 4]))  # Output: 1234


# ------------------------------------------------------------
# 3. Search an item in a list and display the number of occurrences
# ------------------------------------------------------------

def count_occurrences(lst, item):
    return lst.count(item)

# Example:
print("Q3:", count_occurrences([1, 2, 3, 2, 4, 2], 2))  # Output: 3


# ------------------------------------------------------------
# 4. Print even numbers from list until reaching 237 or end
# ------------------------------------------------------------

def even_until_237(lst):
    for num in lst:
        if num == 237:
            break
        if num % 2 == 0:
            print(num, end=" ")

# Example:
print("\nQ4:", end=" ")
even_until_237([10, 15, 22, 33, 44, 237, 50])  # Output: 10 22 44


# ------------------------------------------------------------
# 5. Remove all odd-indexed characters from string
# ------------------------------------------------------------

def remove_odd_index_chars(s):
    return s[::2]  # Take characters at even indices only

# Example:
print("\nQ5:", remove_odd_index_chars("HELLO"))  # Output: HLO


# ------------------------------------------------------------
# 6. Count strings with length ≥ 2 and same first & last character
# ------------------------------------------------------------

def count_special_strings(lst):
    count = 0
    for word in lst:
        if len(word) >= 2 and word[0] == word[-1]:
            count += 1
    return count

# Example:
print("Q6:", count_special_strings(["abc", "ada", "1221", "xy"]))  # Output: 2


# ------------------------------------------------------------
# 7. Count odd and even numbers in a list
# ------------------------------------------------------------

def count_odd_even(lst):
    odd = even = 0
    for num in lst:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
    return odd, even

# Example:
odds, evens = count_odd_even([1, 2, 3, 4, 5, 6])
print("Q7: Odds =", odds, ", Evens =", evens)  # Output: Odds = 3 , Evens = 3


# ------------------------------------------------------------
# 8. Add 'Is' to beginning of string if not already present
# ------------------------------------------------------------

def add_Is(s):
    if s.startswith("Is"):
        return s
    else:
        return "Is" + s

# Example:
print("Q8:", add_Is("happy"))      # Output: Ishappy
print("Q8:", add_Is("IsCool"))     # Output: IsCool


# ------------------------------------------------------------
# 9. Lambda Functions
# ------------------------------------------------------------

# (a) Largest of 2 numbers
largest = lambda a, b: a if a > b else b
print("Q9(a):", largest(10, 20))

# (b) Check if number divisible by 5
div_by_5 = lambda x: x % 5 == 0
print("Q9(b):", div_by_5(25))

# (c) Remove all strings with length < 5
remove_short = lambda lst: [s for s in lst if len(s) >= 5]
print("Q9(c):", remove_short(["hi", "hello", "bye", "python"]))

# (d) Increment list by 10% if >1000 else by 5%
increment = lambda lst: [x * 1.10 if x > 1000 else x * 1.05 for x in lst]
print("Q9(d):", increment([500, 1500, 2000]))


# ------------------------------------------------------------
# 10. Lambda functions to find area of shapes
# ------------------------------------------------------------

area_square = lambda s: s * s
area_rectangle = lambda l, w: l * w
area_triangle = lambda b, h: 0.5 * b * h

print("Q10: Square =", area_square(4),
      ", Rectangle =", area_rectangle(5, 3),
      ", Triangle =", area_triangle(6, 4))


# ------------------------------------------------------------
# 11. Recursive functions
# ------------------------------------------------------------

# (a) Factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# (b) nth Fibonacci number
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# (c) Sum of integer list
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

# Example calls
print("Q11(a): Factorial =", factorial(5))
print("Q11(b): Fibonacci =", fibonacci(7))
print("Q11(c): Sum of list =", sum_list([1, 2, 3, 4, 5]))
print("Q11(d): Sum of first N numbers =", sum_n_numbers(10))
print("Q11(e): Reverse string =", reverse_string("HELLO"))