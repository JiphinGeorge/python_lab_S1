#Python program to find the longest word from a comma-separated list entered by the user


# Find the longest word from a comma-separated list

words = input("Enter words separated by commas: ").split(",")

longest = ""

for w in words:
    w = w.strip()  # remove spaces
    if len(w) > len(longest):
        longest = w

print("The longest word is:", longest)
