from .registration import register
from .ReadData import Read_data
from .WriteData import Write_data
import json

def update_student():
    while True:
        print("===============Update menu==================")
        print("1.Update by id")
        print("2.Back to main menu")
        choice = input("Enter your choice: ")
        data = Read_data()
        if choice.isdigit() and choice in ["1", "2"]:
            if choice == "1":
                id = input("Enter Id to update: ")
                found = False
                for i in range(len(data)):
                    student = data[i]
                    if student['Id'] == id:
                        print("================Enter new details==================")
                        print("1. Update name")
                        print("2. Update address")
                        print("3. Update phone number")
                        print("4. Update all")
                        update_choice = input("Enter your choice: ")
                        if update_choice.isdigit() and update_choice in ["1", "2", "3", "4"]:
                            if update_choice == "1":
                                student['name'] = input("Enter new name: ").title()
                                if student["name"].isalpha():
                                    data[i] = student
                                    Write_data(data)
                                    print("Record updated successfully")
                                else:
                                    print("Invalid input. Please enter a valid name.")
                            elif update_choice == "2":
                                student['Address'] = input("Enter new address: ").title()
                                if student["Address"].isalpha():
                                    data[i] = student
                                    Write_data(data)
                                    print("Record updated successfully")
                                else:
                                    print("Invalid input. Please enter a valid address.")
                            elif update_choice == "3":
                                student['Contact'] = input("Enter new phone number: ")
                                if len(student["Contact"]) == 10 and student["Contact"].isdigit():
                                    data[i] = student
                                    Write_data(data)
                                    print("Record updated successfully")
                                else:
                                    print("Invalid contact number. Please enter a 10-digit number.")
                            elif update_choice == "4":
                                while True:
                                    student["name"] = input("Please enter the name: ").title()
                                    if student["name"].isalpha():
                                        break
                                    else:
                                        print("Invalid input. Please enter a valid name.")
                                while True:
                                    student["Address"] = input("Please enter the address: ").title()
                                    if student["Address"].isalpha():
                                        break
                                    else:
                                        print("Invalid input. Please enter a valid address.")
                                while True:
                                    student["Contact"] = input("Please enter the contact number: ")
                                    if len(student["Contact"]) == 10 and student["Contact"].isdigit():
                                        break
                                    else:
                                        print("Invalid contact number. Please enter a 10-digit number.")
                                data[i] = student
                                Write_data(data)
                                print("Record updated successfully")
                        else:
                            print("Invalid input. Please enter a number between 1 and 4.")
                        found = True
                if not found:
                    print("No record found")
            elif choice == "2":
                return
        else:
            print("Invalid choice. Please enter 1 or 2.")