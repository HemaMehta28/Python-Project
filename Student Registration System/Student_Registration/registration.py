from .ReadData import Read_data
from .WriteData import Write_data
import os
import uuid
import json

existing_data = Read_data()

def register():
    global existing_data
    data = {}
    data["Id"] = uuid.uuid4().hex[:5]
    
    while True:
        data["name"] = input("Please enter the name: ").title()
        if data["name"].isalpha():
            break
        else:
            print("Invalid input. Please enter a valid name.")
    
    while True:
        data["Address"] = input("Please enter the address: ").title()
        if data["Address"].isalpha() :
            break
        else:
            print("Invalid input. Please enter a valid address.")
    
    while True:
        data["Contact"] = input("Please enter the contact number: ")
        if len(data["Contact"]) == 10 and data["Contact"].isdigit():
            contact_exists = False
            for student in existing_data:
                if student["Contact"] == data["Contact"]:
                    print("Contact number already exists. Please enter a different contact number.")
                    contact_exists = True
                    break
            if not contact_exists:
                break
        else:
            print("Invalid contact number. Please enter a 10-digit number.")
    
    try:
        existing_data.append(data)
        Write_data(existing_data)
        print("Registration successful!")
    except Exception as e:
        print(str(e))