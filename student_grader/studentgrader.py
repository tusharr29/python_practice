#Student Grading System

print("Welcome to the student grading system.")

name = input("Enter the student's name: ")
marks = float(input("Enter the student's marks (0-100): "))

if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 60:
    grade = "D"
elif marks >= 50:
    grade = "E"
else:
    grade = "F"

print(f"{name} has received a grade of {grade}.")