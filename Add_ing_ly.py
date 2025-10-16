#Add “ing” or “ly” to a string

word = input("Enter a word: ")

if len(word) >= 3:
    if word.endswith('ing'):
        word += 'ly'
    else:
        word += 'ing'

print("Modified word:", word)
