# Program to copy contents from one file to another

try:
    # Get source and destination file names
    source = input("Enter the source file name: ")
    destination = input("Enter the destination file name: ")

    # Open both files
    with open(source, 'r', encoding='utf-8') as src:
        content = src.read()

    with open(destination, 'w', encoding='utf-8') as dest:
        dest.write(content)

    print(f"File '{source}' copied successfully to '{destination}'.")

except FileNotFoundError:
    print("Error: Source file not found.")
except Exception as e:
    print("An unexpected error occurred:", e)
