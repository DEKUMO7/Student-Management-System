class student:
    def __init__(self, name, age, rollno,course):
        self.name = name
        self.age = age
        self.rollno = rollno
        self.course = course

student_no = 1

while True:
    
    while True:
        name = str(input("Enter Name: ")).strip()
        if name == "":
            print("pleace enetr name first...")
        elif name == name:
            break
    
    if name.lower() == "exit" or name.lower() == "stop" or name.lower() == "quit":
        print("program stopped...")
        break

    if name.lower() == "search student":
        a = input("Enter RollNo: ").strip()
        with open("student.txt","r")as file:
            lines = file.readlines()
        found = False
        for i in range(len(lines)):
            if lines[i].strip() == f"Roll No: {a}":
                print()
                print("STUDENT DETAILS ==>")
                print()
                print(lines[i-3].strip())
                print(lines[i-2].strip())
                print(lines[i-1].strip())
                print(lines[i].strip())
                print(lines[i+1].strip())
                print()
                found = True
                break
        if not found:
            print("student not found...")
        continue
    while True:
        age = (input("Enter Age: ")).strip()
        if age == "":
            print("pleace enetr age first...")
        elif age == age:
            break
    if age.lower() == "exit" or age.lower() == "stop" or age.lower() == "quit":
        print("program stopped...")
        break
    
    if age.lower() == "search student":
        a = input("Enter RollNo: ").strip()
        with open("student.txt","r")as file:
            lines = file.readlines()
        found = False
        for i in range(len(lines)):
            if lines[i].strip() == f"Roll No: {a}":
                print()
                print("STUDENT DETAILS ==>")
                print()
                print(lines[i-3].strip())
                print(lines[i-2].strip())
                print(lines[i-1].strip())
                print(lines[i].strip())
                print(lines[i+1].strip())
                print()
                found = True
                break
        if not found:
            print("student not found...")
        continue

    while True:
        rollno = input("Enter RollNo: ").strip()
        if rollno == "":
            print("pleace enetr rollno first...")
        elif rollno == rollno:
            break
    if rollno.lower() == "exit" or rollno.lower() == "stop" or rollno.lower() == "quit":
        print("program stopped...")
        break
    
    if rollno.lower() == "search student":
        a = input("Enter RollNo: ").strip()
        with open("student.txt","r")as file:
            lines = file.readlines()
        found = False
        for i in range(len(lines)):
            if lines[i].strip() == f"Roll No: {a}":
                print()
                print("STUDENT DETAILS ==>")
                print()
                print(lines[i-3].strip())
                print(lines[i-2].strip())
                print(lines[i-1].strip())
                print(lines[i].strip())
                print(lines[i+1].strip())
                print()
                found = True
                break
        if not found:
            print("student not found...")
        continue

    while True:
        course = input("Enter Course: ").strip()
        if course == "":
            print("pleace enetr course first...")
        elif course == course:
            break
    if course.lower() == "exit" or course.lower() == "stop" or course.lower() == "quit":
        print("program stopped...")
        break
    
    if course.lower() == "search student":
        a = input("Enter RollNo: ").strip()
        with open("student.txt","r")as file:
            lines = file.readlines()
        found = False
        for i in range(len(lines)):
            if lines[i].strip() == f"Roll No: {a}":
                print()
                print("STUDENT DETAILS ==>")
                print()
                print(lines[i-3].strip())
                print(lines[i-2].strip())
                print(lines[i-1].strip())
                print(lines[i].strip())
                print(lines[i+1].strip())
                print()
                found = True
                break
        if not found:
            print("student not found...")
        continue

    student1 = student(name, age, rollno, course)

    try:
        with open("student.txt","r") as file:
            for line in file:
                if line.startswith("Seat No:"):
                    student_no = int(line.split(":")[1].strip()) + 1
    except FileNotFoundError:
            pass

    with open("student.txt","a")as file:
        file.write(f"Seat No: {student_no}\n" f" Name: {student1.name}\n" f" Age: {student1.age}\n" f" Roll No: {student1.rollno}\n" f" Course: {student1.course}\n\n")

    if student_no == 120:
        print("Maximum number of students reached.")
        break
    print("Student Data Successfully Added...")