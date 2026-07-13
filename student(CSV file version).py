import csv

def add_student():
    while True:
        name = input("Enter Student Name: ").strip()
        if name == "":
            print("Please enter a name first...")
        else:
            break
    
    while True:
        roll = input("Enter Student RollNo: ").strip()
        if roll == "":
            print("Please enter a roll number first...")
        else:
            break

    while True:
        age = input("Enter Student Age: ").strip()
        if age == "":
            print("Please enter an age first...")
        else:
            break

    while True:
        course = input("Enter Course: ").strip()
        if course == "":
            print("Please enter a course first...")
        else:
            break

    with open ("student.csv",mode="a",newline="")as file:
        writer = csv.writer(file)
        if file.tell() == 0:
            writer.writerow(['Name', 'Roll No', 'Age', 'Course'])
    
    with open ("student.csv",mode="a",newline="")as file:
        writer = csv.writer(file)
        writer.writerow([name, roll, age, course])

def search_student():
    roll = input("Enter Student RollNo to search: ").strip()
    with open("student.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[1] == roll:
                print(f"Name: {row[0]}, RollNo: {row[1]}, Age: {row[2]}, Course: {row[3]}")
                return
        print("Student not found.")

def delete_student():
    roll = input("Enter Student RollNo to delete: ").strip()
    rows = []
    with open("student.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[1] != roll:
                rows.append(row)
    
    with open("student.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    print("Student deleted if existed.")

def update_student():
    roll = input("Enter Student RollNo to update: ").strip()
    rows = []
    with open("student.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[1] == roll:
                print(f"Current Details - Name: {row[0]}, Roll: {row[1]}, Age: {row[2]}, Course: {row[3]}")
                name = input("Enter new name (or press Enter to keep current): ").strip() or row[0]
                age = input("Enter new age (or press Enter to keep current): ").strip() or row[2]
                course = input("Enter new course (or press Enter to keep current): ").strip() or row[3]
                rows.append([name, roll, age, course])
            else:
                rows.append(row)

    with open("student.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    print("Student updated if existed.")

while True:
    a = input("ADD / STOP / SEARCH / DELETE / UPDATE: ").strip()
    if a.lower() == "add":
        add_student()
        print("Student Information Added Sucessfully......")
        print()
    
    if a.lower() == "stop":
        print("program stoped...")
        break
    
    if a.lower() == "search":
        search_student()

    if a.lower() == "delete":
        delete_student()

    if a.lower() == "update":
        update_student()