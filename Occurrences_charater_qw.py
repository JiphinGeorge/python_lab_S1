#(a) Replace all occurrences of the first character with ‘$’, except the first one

# Get input from user
s = input("Enter a string: ")

# Replace all occurrences of the first character except the first
first_char = s[0]
result = first_char + s[1:].replace(first_char, '$')

print("Modified string:", result)


#(b) Create a string from given string where first and last characters are exchanged
s = input("Enter a string: ")

# Swap first and last characters
if len(s) > 1:
    s = s[-1] + s[1:-1] + s[0]

print("String after swapping:", s)
