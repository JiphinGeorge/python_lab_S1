#(a) Create a single string separated by space from two strings by swapping character at position 1

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

# Swap first character of both strings
new_s1 = s2[0] + s1[1:]
new_s2 = s1[0] + s2[1:]

# Join with space
result = new_s1 + " " + new_s2
print("Result:", result)


#(b) Create a list of colors from comma-separated input and print alternate colors

# Input colors separated by commas
colors = input("Enter colors separated by commas: ").split(',')

# Use slicing to get alternate colors (every 2nd item)
alternate_colors = colors[::2]

print("Alternate colors are:")
for color in alternate_colors:
    print(color.strip())

