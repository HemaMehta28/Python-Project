from .registration import register
from .ReadData import Read_data
import os
import json

def search_student():
    while True:
        print("===============Search menu==================")
        print("1.Search by id")
        print("2.Search by phonenumber")
        print("3.view all record")
        print("4.Back to main menu")
        choice = input("Enter your choice: ")
        if choice.isdigit() and choice in ["1", "2", "3", "4"]:
            data = Read_data()
            if choice == "1":
                id = input("Enter id to search: ")
                found = False
                for student in data:
                    if student['Id'] == id:
                        print(json.dumps(student, indent=4))
                        found = True
                if not found:
                    print("No record found")
            elif choice == "2":
                phonenumber = input("Enter phonenumber to search: ")
                found = False
                for student in data:
                    if student['Contact'] == phonenumber:
                        print(json.dumps(student, indent=4))
                        found = True
                if not found:
                    print("No record found")
            elif choice == "3":
                if data:
                    print(json.dumps(data, indent=4))
                else:
                    print("No record found")
            elif choice == "4":
                return
        else:
            print("Invalid choice. Please enter 1, 2, 3 or 4.")