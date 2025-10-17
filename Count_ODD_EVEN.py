# Program 7: Count Odd and Even Numbers

def count_odd_even(lst):
    odd = even = 0
    for num in lst:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
    return odd, even

# Example
numbers = [int(x) for x in input("Enter numbers: ").split()]
odds, evens = count_odd_even(numbers)
print("Odd numbers:", odds)
print("Even numbers:", evens)
