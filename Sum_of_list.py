# Program to find the sum of elements in a list

numbers = list(map(int, input("Enter numbers separated by commas: ").split(",")))

total = sum(numbers)

print("The sum of elements in the list is:", total)




# Program to find the sum of elements in a list using for loop

numbers = list(map(int, input("Enter numbers separated by commas: ").split(",")))

total = 0

for n in numbers:
    total = total + n

print("The sum of elements in the list is:", total)
