# Write a program that count the number of strings where string length is 2 or more and the first and last characters are same.


Sentence=list(input("Enter a String :").split())


def Count(Sentence):
    count=0
    for i in Sentence:
        if len(i)>2 and i[0]==i[-1]:
            count=count+1
    return count
print("Count of the Number of strings where string length is 2 or more and the first and last characters are same in {} is {}.".format(Sentence,Count(Sentence)))