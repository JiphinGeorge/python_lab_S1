#5. Write a program to remove all odd indexed characters from a given string.

str=input("Enter a String :")


def remove(str):
    return str[::2]

print("The String '{}' after removing all Odd Indexed Charaters is '{}' ".format(str,remove(str)))