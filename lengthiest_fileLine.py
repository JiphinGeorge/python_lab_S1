# The lengthiest line in a file

inf = False

try:
    inf = open('myfile.txt', 'r', encoding='utf-8')
    lines = inf.readlines()
    lines.sort(key=len, reverse=True)
    print("Longest line:\n", lines[0].strip())

except IOError as e:
    print("Error:", e)

finally:
    if inf:
        inf.close()
