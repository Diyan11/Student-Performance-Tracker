import json

students = []

def add_student():
    while True:

        name = input("Enter the name of the student: ")

        if name.strip() == "":
            print("Name cannot be empty. Please enter a valid name.")
        else:
            break

    marks = []

    for i in range (1, 5):
        while True:
            try:
                mark = int (input("Enter the marks for " + str(i) + ": "))
                if mark >= 0 and mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Invalid marks. Please enter marks between 0 and 100.")

            except ValueError:
                print("Please enter a number.")
                
            
    student = {
    "name" : name,
    "marks" : marks
    }
    students.append(student)
    save_students()

    print ("Student added successfully.")

    



def calculate_average(marks):
    return sum(marks) / len(marks)


    

def view_students():
    if len(students) == 0:
        print("No students in the list.")
        return
    
    for student in students:

        total = sum(student["marks"])
        average = calculate_average(student["marks"])
        grade = calculate_grade(average)
        
        print("Student: ", student["name"]) 
        print("Marks: ", student["marks"])
        print("Total= ", total)
        print("Average= ", average)
        print("Grade= ", grade)




def search_student():
    name = input("Enter the name of the student to be searched: ")

    found = False

    for student in students:
        if name.lower() == student["name"].lower():
            print("Student found!")
            print("Student name: ", student["name"])
            print("Student marks= ", student["marks"])
            print("Total marks= ", sum(student["marks"]))

            average = calculate_average(student["marks"])
            print("Student average = ", average)

            grade = calculate_grade(average)

            print("Student grade= ", grade)
            
            found = True
            break

    if found == False:
        print("Student not found.")




def calculate_grade(average):

    grade = "F"
    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >=60:
        grade = "D"

    return grade




def class_average():

    if len(students) == 0:
        print("No students in the list.")
        return
    
    total_average = 0

    for student in students:
    
        total_average += calculate_average(student["marks"])

    class_average = total_average / len(students)

    return class_average




def highest_average():
    highest = 0
    top_student = ""

    if len(students) == 0:
        print("No students in the list.")
        return
    for student in students:
        average = calculate_average(student["marks"])

        if average > highest:
            highest = average
            top_student = student["name"]

    print("Highest average: ", highest)
    print("Top student: ", top_student)




def lowest_average():
    if len(students) == 0:
        print("No students in the list.")
        return

    lowest = calculate_average(students[0]["marks"])
    lowest_student = students[0]["name"]

    for student in students:
        average = calculate_average(student["marks"])

        if average < lowest:
            lowest = average
            lowest_student = student["name"]

    print("Lowest average: ", lowest)
    print("Bottom student: ", lowest_student)


           

def delete_student():
    name = input("Enter the name of the student to be deleted: ")

    found = False

    for student in students:
        if name.lower() == student["name"].lower():
            students.remove(student)
            save_students()
            print("Student deleted successfully.")
            found = True
            break
    if found == False:
        print("Student not found.")




def update_student():
    name = input("Enter the name of the student to be updated: ")

    found = False

    for student in students:
        if name.lower() == student["name"].lower():
            print("Student Found.")
            print("Current marks: ", student["marks"])

            new_marks = []

            for i in range(1, 5):
                while True:
                    try:
                        mark = int (input("Enter new marks for " + str(i) +"): "))

                        if mark >= 0  and mark <= 100:
                            new_marks.append(mark)
                            break
                        else:
                            print("Invalid marks. Please enter marks between 0 and 100.")

                    except ValueError:
                        print("Please enter a number.")

            student["marks"] = new_marks
            save_students()

            print("Student updated successfully.")
            
            found = True
            break
    if found == False:
        print("Student not found.")


def save_students():
    with open("Students.json", "w") as file:
        json.dump(students, file, indent  = 4)

def load_students():
    global students

    try:
        with open("Students.json", "r") as file:
            students = json.load(file)

    except FileNotFoundError:
        print("No saved data found. Starting with an empty list of students.")

load_students()

while True:
    print("====Student Grade Analyzer====")
    print("1. Add student: ")
    print("2. View student: ")
    print("3. Search student: ")                
    print("4. Class average: ")
    print("5. Highest average: ")       
    print("6. Lowest average: ")
    print("7. Delete student: ")
    print("8. Update student: ")
    print("9. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students() 
    elif choice == "3":
        search_student()
    elif choice == "4":
        print("Class average: ", class_average())
    elif choice == "5":
        highest_average()
    elif choice == "6":
        lowest_average()
    elif choice == "7":
        delete_student()
    elif choice == "8":
        update_student()
    elif choice == "9":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")







