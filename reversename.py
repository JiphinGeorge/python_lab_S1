# Program 1: Reverse Full Name
# Accept full name and display it in reverse order with spaces

def reverse_full_name(name):
    words = name.split()          # Split the name into words
    reversed_words = words[::-1]  # Reverse the order of words
    return " ".join(reversed_words)

# Example
full_name = input("Enter your full name: ")
print("Reversed Name:", reverse_full_name(full_name))
