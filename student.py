class student:
    def __init__(self,name,age,rollno):
        self.name = name
        self.age = age
        self.rollno = rollno
    
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Roll No:",self.rollno)
# Example usage
student1 = student("john",20,101)
student1.display()
