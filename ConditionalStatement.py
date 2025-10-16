#(a) Check if a number is even or odd

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")


#(b) Check whether an item is available in a list
items = ['apple', 'banana', 'mango']
item = input("Enter item to search: ")

if item.lower() in items:
    print("Available")
else:
    print("Not Available")
