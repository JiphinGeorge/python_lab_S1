#3. Write a program to search an item in a given list and display the number of occurrences of the given item.

Li =list(input("Enter Items Separated By Commas :").split(","))

item=input("Enter the Item To Search :")

def counts(item,Li):
    count=0
    for i in Li:
        if item == i:
            count=count+1
    return count

print("Number of Occurence Of {} is {}".format(item,counts(item,Li)))

