#5. Generate a string by combining first 2 and last 2 characters
s = input("Enter a string: ")

if len(s) < 2:
    result = ""
elif len(s) == 2:
    result = s + s
else:
    result = s[:2] + s[-2:]

print("Result:", result)
