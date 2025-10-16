#(a) Check if a given key already exists in a dictionary
d = {'a': 1, 'b': 2, 'c': 3}
key = input("Enter key to check: ")

if key in d:
    print("Key exists in dictionary")
else:
    print("Key does not exist")


#(b) Merge two dictionaries
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}

merged = d1.update(d2)
print("Merged dictionary:", merged)
