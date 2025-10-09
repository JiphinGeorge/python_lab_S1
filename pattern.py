n = int(input("Enter the Number of rows of the pyramid: "))

for i in range(1, n + 1):
    print(" "*(n-i),end="")
    print("* "*i)
    
