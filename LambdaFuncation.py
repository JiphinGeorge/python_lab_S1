# Program 9: Lambda Functions

# (a) Largest of two numbers
largest = lambda a, b: a if a > b else b
print("Largest:", largest(10, 20))

# (b) Check if divisible by 5
divisible_by_5 = lambda x: x % 5 == 0
print("Divisible by 5:", divisible_by_5(25))

# (c) Remove strings with length < 5
remove_short = lambda lst: [s for s in lst if len(s) >= 5]
print("Filtered List:", remove_short(["hi", "hello", "bye", "python"]))

# (d) Increment list elements (10% if >1000, else 5%)
increment = lambda lst: [x * 1.10 if x > 1000 else x * 1.05 for x in lst]
print("Incremented List:", increment([500, 1500, 2000]))
