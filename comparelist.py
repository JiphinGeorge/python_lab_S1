#compare two list

list1=list(map(int,input("Enter list 1 : ").split(",")))
list2=list(map(int,input("enter list 2 : ").split(",")))

if list1 == list2:
    print("equal")
else:
    print("Not Equal") 