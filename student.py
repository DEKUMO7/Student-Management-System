while True:
    a = input("Do you want to add student detaails? (y/n):")
    if a == "y":
        class student:
            def __init__(self):
                self.name = input("Enter Name: ")
                self.age = int(input("Enter Age: "))
                self.rollno = int(input("Enter Roll No: "))

    elif a == "n":
        break
    
    student1 = student()

    with open("student.txt","a")as f:
        f.write(f"Name: {student1.name}\nAge: {student1.age}\nRoll No: {student1.rollno}\n")
