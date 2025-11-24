

Student_list = []
print("=================Student Management System=================")

def menu():
    print("\n*****************Menu*******************\n")
    print("1.Add Student")
    print("2.Search Student")
    print("3.Delete Student")
    print("4.Exit")
    print("5.View record\n")

def qualification():
    Qualification = []
    while True:
        qualification = {}
        while True:
            qualification["Qualification_name"] = input("Please enter the Qualification[only contain letter and Numbers]:")
            if qualification["Qualification_name"].isalnum():
                break
            else:
                print("Invalid Qualification name. Please enter only letters and numbers.")
        while True:
            qualification["Passing_year"] = input("Enter the passing year:")
            if qualification["Passing_year"].isdigit() and len(qualification["Passing_year"]) == 4:
                break
            else:
                print("Invalid passing year. Please enter a 4-digit year.")
        Qualification.append(qualification)
        if not Qualification_menu():
            break
    return Qualification


def Qualification_menu():
    print("======Menu=====")
    print("1. Yes")
    print("2. No")
    add=input("Do You want add more qualification: ")
    if add == "1":
        return True
    elif add == "2":
        return False
    else:
        print("Invalid choice. Please enter 1 or 2.")
        return Qualification_menu()


def Add_Student():
    Student_dict = {}
    Student_dict["Id"] = input("Please enter the Id:")
    Student_dict["Name"] = input("Please enter the student name:")
    Student_dict["Address"] = input("Please enter the Address:")
    while True:
        Student_dict["Contact"] = input("Please enter the contact number :")
        if len(Student_dict["Contact"]) == 10 and Student_dict["Contact"].isdigit():
            break
        else:
            print("Invalid contact number. Please enter a 10-digit number.")
    Student_dict["Qualification"]= qualification()
    Student_list.append(Student_dict)




def Search():
    if not Student_list:
        print("No data available.")
        return
    print("****************Menu***********************")
    print("1. Search by name ")
    print("2. Search by contact Number ")
    print("3. Search by Qualification ")
    print("4.Back to menu")
    while True:
        Choice = input("Please enter the choice :")
        if Choice in ["1", "2", "3", "4"]:
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3 or 4.")
    if Choice == "1":
        name = input("Enter the name to search: ")
        found=False
        for items in Student_list:
            if name.lower() == items["Name"].lower():
                found=True
                print(items)
        if not found:
            print("Not Found ")
    elif Choice == "2":
        while True:
            contact = input("Enter the contact to search: ")
            if len(contact) == 10 and contact.isdigit():
                break
            else:
                print("Invalid contact number. Please enter a 10-digit number.")
        found=False
        for items in Student_list:
            if contact == items["Contact"]:
                found=True
                print(items)
        if not found:
            print("Not Found ")
    elif Choice == "3":
        while True:
            print("\n*************************Menu**********************\n")
            print("1.Search by Qualification Name")
            print("2.Search by Qualification with Passing year")
            print("3.Back to main menu")
            Search = input("Please enter the Choice:")
            if Search in ["1", "2", "3"]:
                break
            else:
                print("Invalid choice. Please enter 1, 2 or 3.")
        if Search == "1":
            Qualifications = input("Enter the Qualification to search: ")
            found=False
            for items in Student_list:
                for qualification in items["Qualification"]:
                    if Qualifications.lower() == qualification["Qualification_name"].lower():
                        found=True
                        print(items)
            if not found:
                print("Not Found ")
        elif Search == "2":
            Qualifications = input("Enter the Qualification to search: ")
            while True:
                passing_year = input("Enter the passing year to search: ")
                if passing_year.isdigit() and len(passing_year) == 4:
                    break
                else:
                    print("Invalid passing year. Please enter a 4-digit year.")
            found=False
            for items in Student_list:
                for qualification in items["Qualification"]:
                    if passing_year == qualification["Passing_year"] and Qualifications.lower() == qualification["Qualification_name"].lower():
                        found=True
                        print(items)
            if not found:
                print("Not Found ")
        elif Search == "3":
            pass

def delete():
    if not Student_list:
        print("No data available.")
        return
    id = input("Enter the roll number to delete: ")
    found=False
    for student in Student_list:
        if student["Id"].lower() == id.lower():
            Student_list.remove(student)
            found=True
            print("Student deleted successfully!")
            break
    if not found:
        print("Student not found!")

def Student_Registration():
    while True:
        menu()
        while True:
            choice = input("Enter your choice: ")
            if choice in ["1", "2", "3", "4", "5"]:
                break
            else:
                print("Invalid choice. Please enter 1, 2, 3, 4 or 5.")
        if choice == "1":
            Add_Student()
        elif choice == "2":
            Search()
        elif choice == "3":
            delete()
        elif choice == "4":
            print("***************************Exiting**************************")
            break
        elif choice == "5":
            print(Student_list)

Student_Registration()

