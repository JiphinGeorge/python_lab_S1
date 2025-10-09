#Accept a list of single digit numbers as input string. Concatenate the elements of the list as a single number.

def Concat(Li):
    if not Li:
        return ""
    else:
        return str(Li[0]) + Concat(Li[1:])

Li = list(map(int,input("Enter a list of single-digit numbers separated by Comma : ").split(",")))

print("The Concatenated Version of the List {} is {}".format(Li,  Concat(Li)))
