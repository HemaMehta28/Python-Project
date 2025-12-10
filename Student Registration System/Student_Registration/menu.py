
from .registration import register
from .search import search_student
from .delete import delete_student
from .update import update_student

def studentmenu():
    while True:
        print("=========Student Menu=========\n")
        print("\n1. Register")
        print("2. Search/View Record")
        print("3. Update")
        print("4. Delete")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice.isdigit() and choice in ["1", "2", "3", "4", "5"]:
            if choice == "1":
                register()
            elif choice == "2":
                search_student()
            elif choice == "3":
                update_student()
            elif choice == "4":
                delete_student()
            elif choice == "5":
                break
        else:
            print("Invalid input. Please enter a number between 1 and 5.")