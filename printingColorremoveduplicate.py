#(a) Print colors from color-list1 not contained in color-list2
color_list1 = input("Enter first color list (comma-separated): ").split(',')
color_list2 = input("Enter second color list (comma-separated): ").split(',')

result = [color for color in color_list1 if color not in color_list2]
print("Colors not in list2:", result)


#(b) Remove duplicates from a list

items = input("Enter list elements separated by space: ").split()
unique_items = list(set(items))
print("List without duplicates:", unique_items)

#(c) Check whether a list is empty or not
lst = []
if not lst:
    print("List is empty.")
else:
    print("List is not empty.")
