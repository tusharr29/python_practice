#Highest Scorer in a Class


students = {
    "Amit": 75,
    "Neha": 88,
    "Ravi": 92,
    "Sita": 81
}

topper = max(students, key=students.get)

print("Topper:", topper)
print("Marks:", students[topper])



