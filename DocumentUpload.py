import uuid
import os
import json

list_data = []
def Student():
    dict_data = {
        "id": uuid.uuid4().hex[:6],
        "name": input("Please enter the name: ").title(),
        "address": input("Please enter your address: ").title(),
        "documents": []
    }

    for i in range(3):
        doc_name = input(f"Please Enter the document {i+1} name: ")
        doc_url = input(f"Please enter the URL for {doc_name}: ")
        dict_data["documents"].append({
            "name": doc_name,
            "url": doc_url
        })
    return dict_data

def review_documents(student):
    print(json.dumps(student, indent=4))
    print("=======Menu=======")
    print("1. Submit")
    print("2. Cancel")
    choice = input("Enter your choice: ")
    if choice.isdigit() and choice in ["1", "2"]:
        if choice == "1":
            list_data.clear()  
            list_data.append(student)
            print("Student data saved successfully.")
        elif choice == "2":
            print("Student data not saved.")
    else:
        print("Invalid choice. Please enter 1 ,2 or3.")

        
def main():
    print("======================Student Registration======================")
    temp_student = None
    while True:
        print("*************menu*************")
        print("1. Add Student")
        print("2. Review Documents")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice.isdigit() and choice in ["1", "2","3"]:
            if choice == "1":
                temp_student = Student()

            elif choice == "2":
                if temp_student:
                    review_documents(temp_student)
                    temp_student = None
                elif list_data:
                    for student in list_data:
                        print(json.dumps(student, indent=4))
                        print("\n")
                else:
                    print("No students added .")

            elif choice == "3":
                break

            else:
                print("Invalid choice.")
        else:
            print("Invalid choice. Please enter 1 ,2 or3.")
       


main()
