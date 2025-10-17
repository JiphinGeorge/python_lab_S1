#Add "Is" to beginning of a string (if not already present)


def add_Is(s):
    if s.startswith("Is"):
        return s
    else:
        return "Is" + s

# Example
text = input("Enter a string: ")
print("Result:", add_Is(text))
