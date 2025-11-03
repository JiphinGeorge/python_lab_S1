# Program to remove a specific line from a file

try:
    n = int(input("Enter the line number to remove: "))

    with open("abc.txt", "r+", encoding="utf-8") as inf:
        lines = inf.readlines()

        if 1 <= n <= len(lines):
            lines.pop(n - 1)           # remove nth line
            inf.seek(0)                # move cursor to start
            inf.truncate()             # clear file content
            inf.writelines(lines)      # write back updated content
            print(f"Line {n} removed successfully.")
        else:
            print("Invalid line number.")

except FileNotFoundError:
    print("Error: File not found.")
except ValueError:
    print("Please enter a valid number.")
except Exception as e:
    print("An unexpected error occurred:", e)
