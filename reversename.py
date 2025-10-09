#Accept full name and display in reverse order with space between the words.

name=input("Enter a Name :")

def rev(name):
    if name == "":
        return ""
    else:
        return name[-1]+" " + rev(name[:-1])

print("Reversed Name '{}' is '{}':".format(name ,rev(name)))