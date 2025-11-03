try:
    src = input("Enter source file name: ")
    dest = input("Enter destination file name: ")

    with open(src, "r") as f1, open(dest, "w") as f2:
        for line in f1:
            if not line.strip().startswith("#") and line.strip() != "":
                f2.write(line)

    print("Comments removed successfully!")

except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print("An error occurred:", e)
