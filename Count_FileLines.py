# Program to count the number of lines in a file

# Ask the user for the file name
filename = input("Enter the file name: ")

try:
    # Open the file in read mode
    with open(filename, 'r') as file:
        # Read all lines into a list
        lines = file.readlines()
        # Count the lines
        line_count = len(lines)

    print(f"Number of lines in '{filename}': {line_count}")

except FileNotFoundError:
    print("Error: File not found. Please check the file name and try again.")
except Exception as e:
    print("An error occurred:", e)
