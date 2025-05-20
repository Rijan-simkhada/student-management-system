def add_students():
    user_name = input("Enter student name: ")
    user_age = input("Enter student age: ")
    user_class = input("Enter student class: ")
    user_phone = input("Enter student phone: ")
    with open("Student Management/student.txt","a") as f:
        f.write(f"{user_name},{user_age},{user_class},{user_phone}\n")
    print("---Student Details Save Sucessfully---")


def view_student():
    with open("Student Management/student.txt", "r") as f:
        print("\n--- All Students ---\n")
        for line in f:
            name, age, grade, phone = line.strip().split(",")
            print(f"Name: {name} | Age: {age} | Class: {grade} | Phone: {phone}")

def search_student():
   keyword = input("Enter name or phone number to search: ").lower()
   found = False
   with open("Student Management/student.txt", "r") as f:
        for line in f:
            name, age, grade, phone = line.strip().split(",")

            if keyword in name.lower() or keyword in phone:
                print(f"Name: {name} | Age: {age} | Class: {grade} | Phone: {phone}")
                found = True
    
        if not found:
             print("No student found with that keyword.")

def delete_student():
    keyword = input("Enter student name or phone to delete: ").lower()
    found = False
    
    with open("Student Management/student.txt", "r") as f:
        lines = f.readlines()
    
    with open("Student Management/student.txt", "w") as f:
        for line in lines:
            name, age, grade, phone = line.strip().split(",")
            if keyword != name.lower() and keyword != phone:
                f.write(line)
            else:
                found = True
    
    if found:
        print("Student record deleted successfully.")
    else:
        print("No matching student found.")


   



while True:
    
    print("\n<<-Enter your choice->>\n1. Add Student\n2. View All\n3. Search Student\n4. Delete Records\n5. Exit")
    

    user = int(input("Enter Your Choice: "))
    if user == 1:
        print("\n---To Add Student Details Fill All of the Follwing Details---\n")
        add_students()
    elif user == 2:
        view_student()
    elif user == 3:
        search_student()
    elif user == 4:
        delete_student()
    elif user ==5:
        print("---good byee---")
        break
    else:
        print("<<<Enter valid numbers>>>")

