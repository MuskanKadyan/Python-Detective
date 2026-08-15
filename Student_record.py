print("Menu")
choice = int(input("Enter your choice: "))
if choice == 1:
    print("Add Student Selected")

elif choice == 2:
    print("View Student Selected")

elif choice == 3:
    print("Search Student Selected")

elif choice == 4:
    print("Update Student Selected")

elif choice == 5:
    print("Delete Student Selected")

elif choice == 6:
    print("Thank you!")

else:
    print("Invalid Choice")

student_id = input("Enter Student ID: ")
name = input("Enter Name: ")
age = input("Enter Age: ")
course = input("Enter Course: ")
email = input("Enter Email: ")

with open("stdents.csv","append",newline="") as file:
    writer = csv.writer(file)
    writer.writerow([student_id,name,age,course,email])
    print("Student added sucessfully!")

    open("students.csv","a",newline="")