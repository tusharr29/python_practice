#Students Marks Management System

student_marks = {}

def add_info():
    name = input("Enter the student's name: ")
    marks = float(input(f"Enter the marks obtained by {name} out of 100: "))
    roll_no = int(input("Enter the roll number of the student: "))
    subject = input("Enter the subject name: ")

    student_marks[name] = {
        'Roll Number': roll_no,
        'Subject': subject,
        'Marks': marks
    }

    print(f"Information for {name} added successfully.")

def view_info():
    name = input("Enter the student's name to view information:")
    if not student_marks:
        print("No student information available.")
        return
    elif name in student_marks:
        info = student_marks[name]
        print(f"Information for {name}:")
        print(f"Roll Number: {info['Roll Number']}")
        print(f"Subject: {info['Subject']}")
        print(f"Marks: {info['Marks']}/100.0")
    else:
        print(f"No information found for student named {name}.")
    
def remove_info():
    name = input("Enter the student's name to remove information:")
    if name in student_marks:
        student_marks.pop(name)
        print(f"Information for {name} removed successfully.")
    else:
        print(f"No information found for student named {name}.")
    
def  modify_info():
    name = input("Enter the student's name to modify information:")
    if name in student_marks:
        info = input("Enter the field to modify (Roll Number/Subject/Marks): ").lower()
        if info in student_marks[name]:
            new_value = input(f"Enter the new value for {info}: ")
            if info == 'marks':
                new_value = float(new_value)
            elif info == 'roll Number':
                new_value = int(new_value)
            elif info == 'subject':
                new_value = str(new_value)
            student_marks[name][info] = new_value
            print(f"{info} for {name} updated successfully.")
        else:
            print(f"Invalid field: {info}.")
    else:
        print(f"No information found for student named {name}.")

def find_topper():
    if not student_marks:
        print("No student information available.")
        return

    topper = max(student_marks.items(), key=lambda x: x[1]['Marks'])
    name, info = topper
    print(f"The topper is {name} with {info['Marks']}/100.0 marks.")

def sort_marks():
    if not student_marks:
        print("No student information available.")
        return

    sorted_students = sorted(student_marks.items(), key=lambda x: x[1]['Marks'], reverse=True)
    print("Students sorted by marks (highest to lowest):")
    for name, info in sorted_students:
        print(f"{name}: {info['Marks']}/100.0")

while True:
    print("\nStudent Marks Management System\n")
    print("1. Add Student Information")
    print("2. View Student Information")
    print("3. Remove Student Information")
    print("4. Modify Student Information")
    print("5. Find Topper")
    print("6. Sort Students by Marks")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == '1':
        add_info()
    elif choice == '2':
        if view_info()==None:
            print("No data found.")
        else:
            view_info()
    elif choice == '3':
        remove_info()
    elif choice == '4':
        modify_info()
    elif choice == '5':
        find_topper()
    elif choice == '6':
        sort_marks()
    elif choice == '7':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")



