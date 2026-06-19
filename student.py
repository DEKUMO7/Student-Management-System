class student:
    def __init__(self, name, age, rollno):
        self.name = name
        self.age = age
        self.rollno = rollno

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

    student1 = student()

    with open("student.txt","a")as file:
        file.write(f"Name: {student1.name}\nAge: {student1.age}\nRoll No: {student1.rollno}\n")
