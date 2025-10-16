#(a) Generate positive numbers from a given list
nums = [-3, -1, 0, 2, 5, -6]
positive = [n for n in nums if n > 0]
print("Positive numbers:", positive)



#b) Generate list with squares of numbers
nums = [1, 2, 3, 4, 5]
squares = [n**2 for n in nums]
print("Squares:", squares)

#(c) Form a list containing vowels from a given word
word = input("Enter a word: ")
vowels = [ch for ch in word if ch.lower() in 'aeiou']
print("Vowels:", vowels)


#(d) Generate a list by removing even numbers
nums = [1, 2, 3, 4, 5, 6]
odd_nums = [ n for n in nums if n%2!=0]
print("List without even numbers:", odd_nums)


#(e) Display leap years from current to future year
current = int(input("Enter current year: "))
future = int(input("Enter future year: "))

leap_years = [year for year in range(current, future + 1) if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)]

print("Leap years:", leap_years)

