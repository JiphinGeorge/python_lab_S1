#4. Write a program to print all even numbers from a given list in the given order until you reach number 237 or end of the list.

numList =list(map(int,input("Enter a list of Numbers Separated By Commas :").split(",")))

def finder(numList):
    ListEven=[]
    for i in numList:
        if i ==237:
            break
        else:
            if i%2==0:
                ListEven.append(i)
    return ListEven
print("The Even Numbers From the List {} is {}".format(numList,finder(numList)))