
from .registration import register
from .ReadData import Read_data
from .WriteData import Write_data
import json
import os
def delete_student():
    while True:
        print("===============Delete Menu===================")
        print("1.Delete student by Id")
        print("2.Back to main menu")
        choice = input("Enter your choice: ")
        data = Read_data()
        if choice.isdigit() and choice in ["1", "2"]:
            if choice == "1":
                id = input("Enter id to delete: ")
                new_data = []
                deleted = False
                for student in data:
                    if student['Id'] != id:
                        new_data.append(student)
                    else:
                        deleted = True
                Write_data(new_data)
                if deleted:
                    print("Student deleted successfully")
                else:
                    print("Student not found")
            elif choice == "2":
                return
        else:
            print("Invalid input. Please enter 1 and 2.")