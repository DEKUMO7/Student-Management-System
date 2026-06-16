class student:
    def __init__(self):
        self.name = input("Enter Name: ")
        self.age = int(input("Enter Age: "))
        self.rollno = int(input("Enter Roll No: "))
    
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Roll No:",self.rollno)
# Example usage
student1 = student()

with open("student.txt","a")as f:
    f.write(f"{student1.name}\n{student1.age}\n{student1.rollno}\n")
