from admin_module import admin_login, admin_menu
from student_module import student_menu

def display_welcome_message():
    print("******   Welcome to Real Champions Sports Academy   ******")

def choose_user_role():
    while True:
        display_welcome_message()
        print("Select User Role:")
        print("1. Admin")
        print("2. Student")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            if admin_login():
                admin_menu()
        elif choice == "2":
            student_menu()
        elif choice == "3":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

def main():
    choose_user_role()

if __name__ == "__main__":
    main()