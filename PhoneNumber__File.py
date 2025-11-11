# Write a Python program to retrieve phone numbers from a file.
# Phone numbers must start with 6, 7, 8, or 9 and must be exactly 10 digits long.

import re

filename = input("Enter file name: ")

try:
    f = open(filename, "r")
    text = f.read()
    f.close()

    # Regular expression: starts with 6/7/8/9 and followed by 9 more digits
    numbers = re.findall(r'\b[6-9]\d{9}\b', text)

    print("Valid Phone Numbers Found:")
    for num in numbers:
        print(num)

except FileNotFoundError:
    print("File not found.")