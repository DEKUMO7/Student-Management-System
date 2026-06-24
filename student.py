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

    while True:
        age = (input("Enter Age: ")).strip()
        if age == "":
            print("pleace enetr age first...")
        elif age == age:
            break
    if age.lower() == "exit" or age.lower() == "stop" or age.lower() == "quit":
        print("program stopped...")
        break
    
    while True:
        rollno = input("Enter RollNo: ").strip()
        if rollno == "":
            print("pleace enetr rollno first...")
        elif rollno == rollno:
            break
    if rollno.lower() == "exit" or rollno.lower() == "stop" or rollno.lower() == "quit":
        print("program stopped...")
        break

    while True:
        course = input("Enter Course: ").strip()
        if course == "":
            print("pleace enetr course first...")
        elif course == course:
            break
    if course.lower() == "exit" or course.lower() == "stop" or course.lower() == "quit":
        print("program stopped...")
        break

    student1 = student(name, age, rollno, course)

    with open("student.txt","a")as file:
        file.write(f"Seat No: {student_no}\n Name: {student1.name}\nAge: {student1.age}\nRoll No: {student1.rollno}\nCourse: {student1.course}\n\n")

    if student_no == 120:
        print("Maximum number of students reached.")
        break
    student_no += 1