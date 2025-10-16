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

d1.update(d2) # or use  d1 | d2  
print("Merged dictionary:", d1)




#(c) Sort dictionary in ascending and descending order
d = {'b': 2, 'a': 3, 'c': 1}

asc = dict(sorted(d.items()))
desc = dict(sorted(d.items(), reverse=True))

print("Ascending:", asc)
print("Descending:", desc)




#(d) Create an inverted dictionary
d = {'a': 1, 'b': 2, 'c': 3}
inverted = {}

for k, v in d.items():
    inverted[v] = k

print("Inverted dictionary:", inverted)

