#accept a list of numbers from user . create a new list with numbers greater than 100 from the input list using list comprehesion


# Accept a list of numbers from user
numbers = list(map(int, input("Enter numbers separated by commas: ").split(",")))

# Create a new list with numbers greater than 100 using list comprehension
greater_than_100 = [x for x in numbers if x>100]

print("Numbers greater than 100:", greater_than_100)
