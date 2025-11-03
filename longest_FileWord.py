# Program to find the longest word in a file

try:
    # Ask user for the file name
    filename = input("Enter the file name: ")

    with open(filename, 'r', encoding='utf-8') as file:
        # Read entire file content
        content = file.read()

        # Split the text into words
        words = content.split()

        if not words:
            print("The file is empty.")
        else:
            # Find the longest word
            longest_word = max(words, key=len)
            print("\nLongest word:")
            print(longest_word)
            print(f"\nLength: {len(longest_word)} characters")

except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print("An unexpected error occurred:", e)
