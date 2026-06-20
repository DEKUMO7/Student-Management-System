class student:
    def __init__(self, name, age, rollno,course):
        self.name = name
        self.age = age
        self.rollno = rollno
        self.course = course

student_no = 1

while True:
    name = input("Enter Name: ")
    if name.lower() == "exit" or name.lower() == "stop" or name.lower() == "quit":
        print("program stopped")
        break
    age = input("Enter Age: ")
    if age.lower() == "exit" or age.lower() == "stop" or age.lower() == "quit":
        print("program stopped")
        break
    rollno = input("Enter Roll No: ")
    if rollno.lower() == "exit" or rollno.lower() == "stop" or rollno.lower() == "quit":
        print("program stopped")
        break
    
    course = input("Enter Course: ")
    if course.lower() == "exit" or course.lower() == "stop" or course.lower() == "quit":
        print("program stopped")
        break
    student1 = student(name, age, rollno, course)

    with open("student.txt","a")as file:
        file.write(f"Seat No: {student_no}\n Name: {student1.name}\nAge: {student1.age}\nRoll No: {student1.rollno}\nCourse: {student1.course}\n\n")

    if student_no == 120:
        print("Maximum number of students reached.")
        break
    student_no += 1