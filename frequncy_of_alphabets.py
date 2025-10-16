#(a) Determine frequency of alphabets in a word

# Program to find frequency of alphabets using count()

word = input("Enter a word: ")

for ch in set(word):   # set() removes duplicates
    print(ch, ":", word.count(ch))


#(b) Create a list of first names and count names starting with ‘a’
names = input("Enter first names separated by space: ").split()
count = sum(1 for name in names if name.lower().startswith('a'))

print("List of names:", names)
print("Number of names starting with 'a':", count)


#(c) Count each word in a line of text
text = input("Enter a line of text: ").split()
count = len(text)
print("Number of words:", count)
