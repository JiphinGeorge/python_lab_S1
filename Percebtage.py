#6. Accept percentage of marks and display grade
marks = float(input("Enter your percentage: "))

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B+"
elif marks >= 60:
    grade = "B"
elif marks >= 50:
    grade = "C"
else:
    grade = "Fail"

print("Grade:", grade)
