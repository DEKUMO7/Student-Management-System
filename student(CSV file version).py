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

    with open ("student.csv","a",newline="")as file:
        writer = csv.writer(file)
        writer.writerow([name,roll,age,course])



while True:
    a = input("ADD / STOP / SEARCH / DELETE / UPDATE: ").strip()
    if a.lower() == "add":
        add_student()

    if a.lower() == "stop":
        print("program stoped...")
        break
