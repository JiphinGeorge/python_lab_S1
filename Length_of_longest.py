#Accept a string and return the length of the longest word if the result has more than one word then print "BINGO"

sentence = input("Enter a sentence: ")
words = sentence.split()
longest = max(words, key=len)
length = len(longest)

print("Longest word:", longest)
if sum(len(w) == length for w in words) > 1:
    print("BINGO")
