Student_list = []

def menu():
    print("*****************Menu*******************")
    print("1.Add Student")
    print("2.Search Student")
    print("3.Delete Student")
    print("4.Exit")
    print("5.View record")
    
def Add_Student():
    Student_dict = {}
    Student_dict["Id"] = int(input("Please enter the Id:"))
    Student_dict["Name"] = input("Please enter the student name:")
    Student_dict["Address"] = input("Please enter the Address:")
    Student_dict["Contact"] = int(input("Please enter the contact number :"))
    Qualification = []
    qualification = {}
    qualification["Qualification_name"] = input("Please enter the Qualification:")
    qualification["Passing_year"] = int(input("Enter the passing year:"))
    Qualification.append(qualification)
    totalQualification = int(input("How many more qualifications do you want to add? "))
    for item in range(totalQualification):
        qualification = {}
        qualification["Qualification_name"] = input("Please enter the Qualification:")
        qualification["Passing_year"] = int(input("Enter the passing year:"))
        Qualification.append(qualification)
    Student_dict["Qualification"] = Qualification
    Student_list.append(Student_dict)



def Search():
    print("****************Menu***********************")
    print("1. Search by name: ")
    print("2. Search by contact Number: ")
    print("3. Search by Qualification :")
    Choice = int(input("Please enter the choice :"))
    if Choice == 1:
        name = input("Enter the name to search: ")
        for items in Student_list:
            if name.lower() == items["Name"].lower():
                print(items)
    elif Choice == 2:
        contact = int(input("Enter the contact to search: "))
        for items in Student_list:
            if contact == items["Contact"]:
                print(items)
    elif Choice == 3:
        while True:
            print("\n*************************Menu**********************\n")
            print("1.Search by Qualification")
            print("2.Search by Qualification with Passing year")
            print("3.Back to main menu")
            Search = int(input("Please enter the Choice:"))
            if Search == 1:
                Qualifications = input("Enter the Qualification to search: ")
                for items in Student_list:
                    for qualification in items["Qualification"]:
                        if Qualifications.lower() == qualification["Qualification_name"].lower():
                            print(items)
            elif Search == 2:
                Qualifications = input("Enter the Qualification to search: ")
                passing_year = int(input("Enter the passing year to search: "))
                for items in Student_list:
                    for qualification in items["Qualification"]:
                        if passing_year == qualification["Passing_year"] and Qualifications.lower() == qualification["Qualification_name"].lower():
                            print(items)
            elif Search == 3:
                break
            else:
                print("invalid choice")



def delete():
    roll_number = input("Enter the roll number to delete: ")
    for student in Student_list:
        if student["Id"] == int(roll_number):
            Student_list.remove(student)
            print("Student deleted successfully!")
            break
    else:
        print("Student not found!")




while True:
    menu()
    choice = int(input("Enter your choice: "))
    if choice == 1:
        Add_Student()
    elif choice == 2:
        Search()
    elif choice == 3:
        delete()
    elif choice == 4:
        print("***************************Exiting**************************")
        break
    elif choice == 5:
        print(Student_list)
    else:
        print("Invalid choice")