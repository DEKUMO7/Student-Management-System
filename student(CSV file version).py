import csv

def add_student():
    name = input("Enter Student Name: ")
    roll = input("Enter Student RollNo: ")
    age = input("Enter Student Age: ")
    course = input("Enter Course: ")

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
