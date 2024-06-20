ADMINS_FILE = "files/admins.txt"
COACHES_FILE = "files/coaches.txt"
SPORTS_FILE = "files/sports.txt"
SCHEDULE_FILE = "files/sport_schedule.txt"
REGISTERED_STUDENTS_FILE = "files/registered_students.txt"

def read_admin_credentials():
    admin_credentials = {}
    try:
        with open(ADMINS_FILE, "r") as file:
            for line in file:
                username, password = line.strip().split(',')
                admin_credentials[username] = password
    except FileNotFoundError:
        print(f"File {ADMINS_FILE} not found.")
    except Exception as e:
        print(f"An error occurred while reading admin credentials: {str(e)}")

    return admin_credentials

def admin_login():
    admin_credentials = read_admin_credentials()
    while True:
        username = input("Enter Admin Username: ")
        password = input("Enter Password: ")

        if admin_credentials.get(username) == password:
            print("Login Successful!")
            return True
        else:
            print("Invalid username or password. Please try again.")

def admin_menu():
    while True:
        print("\nAdmin Menu:")
        print("1. Add")
        print("2. Display")
        print("3. Search")
        print("4. Modify")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_menu()
        elif choice == "2":
            display_menu()
        elif choice == "3":
            search_menu()
        elif choice == "4":
            modify_menu()
        elif choice == "5":
            return "exit"
        else:
            print("Invalid choice. Please try again.")

def add_menu():
    while True:
        print("\nAdd Menu:")
        print("1. Add Coach")
        print("2. Add Sport")
        print("3. Add Sport Schedule")
        print("4. Back")

        sub_choice = input("Enter your choice: ")

        if sub_choice == "1":
            add_coach()
        elif sub_choice == "2":
            add_sport()
        elif sub_choice == "3":
            add_sport_schedule()
        elif sub_choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

def display_menu():
    while True:
        print("\nDisplay Menu:")
        print("1. Display All Coaches")
        print("2. Display All Sports")
        print("3. Display Registered Students")
        print("4. Back")

        sub_choice = input("Enter your choice: ")

        if sub_choice == "1":
            display_all_coaches()
        elif sub_choice == "2":
            display_all_sports()
        elif sub_choice == "3":
            display_registered_students()
        elif sub_choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

def search_menu():
    while True:
        print("\nSearch Menu:")
        print("1. Search Coach")
        print("2. Search Sport")
        print("3. Search Student")
        print("4. Back")

        sub_choice = input("Enter your choice: ")

        if sub_choice == "1":
            search_coach_menu()
        elif sub_choice == "2":
            search_sport_by_id()
        elif sub_choice == "3":
            search_student_by_id()
        elif sub_choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

def search_coach_menu():
    while True:
        print("\nSearch Coach Menu:")
        print("1. By Overall Performance (Rating)")
        print("2. By Coach ID")
        print("3. Back")

        search_choice = input("Enter your choice: ")

        if search_choice == "1":
            search_coach_by_rating()
        elif search_choice == "2":
            coach_id = input("Enter Coach ID to search: ")
            search_coach_by_id(coach_id)
        elif search_choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

def modify_menu():
    while True:
        print("\nModify Menu:")
        print("1. Modify Coach")
        print("2. Modify Sport")
        print("3. Modify Sport Schedule")
        print("4. Back")

        sub_choice = input("Enter your choice: ")

        if sub_choice == "1":
            modify_coach_by_id()
        elif sub_choice == "2":
            modify_sport_by_id()
        elif sub_choice == "3":
            modify_sport_schedule()
        elif sub_choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

def check_duplicate_coach_id(coach_id):
    try:
        with open(COACHES_FILE, "r") as file:
            for line in file:
                existing_coach_id, *_ = line.strip().split(',')
                if existing_coach_id == coach_id:
                    return True
    except FileNotFoundError:
        pass
    return False

def add_coach():
    while True:
        coach_id = input("Enter Coach ID: ")
        if check_duplicate_coach_id(coach_id):
            print("Coach with this ID already exists. Please enter a unique Coach ID.")
        else:
            break

    name = input("Enter Coach Name: ")
    date_joined = input("Enter Date Joined: ")
    date_terminated = input("Enter Date Terminated (leave empty if not terminated): ")
    hourly_rate = input("Enter Hourly Rate: ")
    phone = input("Enter Phone: ")
    address = input("Enter Address: ")
    sport_centre_code = input("Enter Sport Centre Code: ")
    sport_center_name = input("Enter Sport Center Name: ")
    sport_code = input("Enter Sport Code: ")
    sport_name = input("Enter Sport Name: ")
    rating = input("Enter Rating (1 to 5): ")

    coach_data = f"{coach_id},{name},{date_joined},{date_terminated or 'N/A'},{hourly_rate},{phone},{address},{sport_centre_code},{sport_center_name},{sport_code},{sport_name},{rating}"
    try:
        with open(COACHES_FILE, "a") as file:
            file.write(coach_data + "\n")
        print("Coach added successfully.")
    except Exception as e:
        print(f"An error occurred while adding coach: {str(e)}")

def check_duplicate_sport_id(sport_id):
    try:
        with open(SPORTS_FILE, "r") as file:
            for line in file:
                existing_sport_id, *_ = line.strip().split(',')
                if existing_sport_id == sport_id:
                    return True
    except FileNotFoundError:
        pass
    return False

def add_sport():
    while True:
        sport_id = input("Enter Sport ID: ")
        if check_duplicate_sport_id(sport_id):
            print("Sport with this ID already exists. Please enter a unique Sport ID.")
        else:
            break

    sport_name = input("Enter Sport Name: ")

    sport_data = f"{sport_id},{sport_name}"
    try:
        with open(SPORTS_FILE, "a") as file:
            file.write(sport_data + "\n")
        print("Sport added successfully.")
    except Exception as e:
        print(f"An error occurred while adding sport: {str(e)}")

def add_sport_schedule():
    try:
        sport_schedule_id = input("Enter Sport Schedule ID: ")
        sport_centre = input("Enter Sport Centre: ")
        coach_id = input("Enter Coach ID: ")
        day = input("Enter Day (e.g., Monday): ")
        time = input("Enter Time (e.g., 10:00 AM): ")

        schedule_data = f"{sport_schedule_id},{sport_centre},{coach_id},{day},{time}"

        with open(SCHEDULE_FILE, "a") as file:
            file.write(schedule_data + "\n")
        print("Sport Schedule added successfully.")
    except Exception as e:
        print(f"An error occurred while adding sport schedule: {str(e)}")

def display_all_coaches():
    try:
        with open(COACHES_FILE, "r") as file:
            next(file)
            for line in file:
                coach_data = line.strip().split(',')
                display_coach_data(coach_data)
    except FileNotFoundError:
        print("Coaches data file not found.")
    except Exception as e:
        print(f"An error occurred while displaying coaches: {str(e)}")

def display_all_sports():
    try:
        with open(SPORTS_FILE, "r") as file:
            next(file)
            for line in file:
                sport_data = line.strip().split(',')
                print(f"Sport ID: {sport_data[0]}")
                print(f"Sport Name: {sport_data[1]}\n")
    except FileNotFoundError:
        print("Sports data file not found.")
    except Exception as e:
        print(f"An error occurred while displaying sports: {str(e)}")

def display_registered_students():
    try:
        with open(REGISTERED_STUDENTS_FILE, "r") as file:
            for line in file:
                student_data = line.strip().split(',')
                if len(student_data) == 6:
                    display_student_data(student_data)
                else:
                    print("Invalid data format in the file.")
    except FileNotFoundError:
        print("Registered students data file not found.")
    except Exception as e:
        print(f"An error occurred while displaying registered students: {str(e)}")

def modify_coach_by_id():
    target_coach_id = input("Enter Coach ID to modify: ")
    try:
        coach_data_list = []
        found = False

        with open(COACHES_FILE, "r") as file:
            for line in file:
                coach_data = line.strip().split(',')
                coach_id = coach_data[0]

                if coach_id == target_coach_id:
                    found = True
                    print(f"Current Coach Data for ID {target_coach_id}:")
                    display_coach_data(coach_data)
                    updated_coach_data = prompt_for_coach_data(coach_data)
                    coach_data_list.append(updated_coach_data)
                else:
                    coach_data_list.append(coach_data)

        if not found:
            print(f"Coach with ID {target_coach_id} not found.")
        else:
            with open(COACHES_FILE, "w") as file:
                for coach_data in coach_data_list:
                    file.write(','.join(coach_data) + '\n')
            print(f"Coach with ID {target_coach_id} updated successfully.")

    except FileNotFoundError:
        print("Coaches data file not found.")
    except Exception as e:
        print(f"An error occurred while modifying coach: {str(e)}")

def prompt_for_coach_data(coach_data):
    fields = ["Coach ID", "Name", "Date Joined", "Date Terminated", "Hourly Rate", "Phone", "Address", "Sport Centre Code", "Sport Center Name", "Sport Code", "Sport Name", "Rating"]
    updated_data = []
    for i, field in enumerate(fields):
        value = input(f"Enter updated {field} (press Enter to keep existing, current: {coach_data[i]}): ")
        updated_data.append(value if value else coach_data[i])
    return updated_data

def modify_sport_by_id():
    target_sport_id = input("Enter Sport ID to modify: ")
    try:
        sport_data_list = []
        found = False

        with open(SPORTS_FILE, "r") as file:
            for line in file:
                sport_data = line.strip().split(',')
                sport_id = sport_data[0]

                if sport_id == target_sport_id:
                    found = True
                    print(f"Current Sport Data for ID {target_sport_id}:")
                    print(f"Sport ID: {sport_data[0]}")
                    print(f"Sport Name: {sport_data[1]}")
                    sport_name = input("Enter updated Sport Name (press Enter to keep existing): ")
                    sport_data_list.append([sport_id, sport_name if sport_name else sport_data[1]])
                else:
                    sport_data_list.append(sport_data)

        if not found:
            print(f"Sport with ID {target_sport_id} not found.")
        else:
            with open(SPORTS_FILE, "w") as file:
                for sport_data in sport_data_list:
                    file.write(','.join(sport_data) + '\n')
            print(f"Sport with ID {target_sport_id} updated successfully.")

    except FileNotFoundError:
        print("Sports data file not found.")
    except Exception as e:
        print(f"An error occurred while modifying sport: {str(e)}")

def modify_sport_schedule():
    schedule_id = input("Enter the Sport Schedule ID to modify: ")
    try:
        schedule_data_list = []
        found = False

        with open(SCHEDULE_FILE, "r") as file:
            for line in file:
                schedule_data = line.strip().split(',')
                if schedule_data[0] == schedule_id:
                    found = True
                    print(f"Current Schedule Data for ID {schedule_id}:")
                    print(schedule_data)
                    updated_schedule_data = prompt_for_schedule_data(schedule_data)
                    schedule_data_list.append(updated_schedule_data)
                else:
                    schedule_data_list.append(schedule_data)

        if not found:
            print(f"Sport Schedule with ID {schedule_id} not found.")
        else:
            with open(SCHEDULE_FILE, "w") as file:
                for schedule_data in schedule_data_list:
                    file.write(','.join(schedule_data) + '\n')
            print(f"Sport Schedule with ID {schedule_id} updated successfully.")

    except FileNotFoundError:
        print("Sport Schedules data file not found.")
    except Exception as e:
        print(f"An error occurred while modifying sport schedule: {str(e)}")

def prompt_for_schedule_data(schedule_data):
    fields = ["Sport Schedule ID", "Sport Centre", "Coach ID", "Day", "Time"]
    updated_data = []
    for i, field in enumerate(fields):
        value = input(f"Enter updated {field} (press Enter to keep existing, current: {schedule_data[i]}): ")
        updated_data.append(value if value else schedule_data[i])
    return updated_data

def search_sport_by_id():
    target_sport_id = input("Enter Sport ID to search: ")
    try:
        with open(SPORTS_FILE, "r") as file:
            next(file)
            for line in file:
                sport_data = line.strip().split(',')
                if sport_data[0] == target_sport_id:
                    print(f"Sport ID: {sport_data[0]}")
                    print(f"Sport Name: {sport_data[1]}\n")
                    return
        print(f"Sport with ID {target_sport_id} not found.")
    except FileNotFoundError:
        print("Sports data file not found.")
    except Exception as e:
        print(f"An error occurred while searching sport: {str(e)}")

def search_coach_by_rating():
    target_rating = input("Enter the rating (1 to 5) to search for coaches: ")
    try:
        found_coaches = []
        with open(COACHES_FILE, "r") as file:
            next(file)
            for line in file:
                coach_data = line.strip().split(',')
                if coach_data[-1] == target_rating:
                    found_coaches.append(coach_data)

        if found_coaches:
            print(f"Coaches with rating {target_rating}:")
            for coach in found_coaches:
                display_coach_data(coach)
        else:
            print(f"No coaches found with rating {target_rating}.")

    except FileNotFoundError:
        print("Coaches data file not found.")
    except Exception as e:
        print(f"An error occurred while searching coaches: {str(e)}")

def search_coach_by_id(coach_id):
    try:
        coach_data = find_coach_by_id(coach_id)
        if coach_data:
            display_coach_data(coach_data)
        else:
            print(f"Coach with ID {coach_id} not found.")
    except FileNotFoundError:
        print("Coaches data file not found.")
    except Exception as e:
        print(f"An error occurred while searching coach: {str(e)}")

def find_coach_by_id(coach_id):
    try:
        with open(COACHES_FILE, "r") as file:
            for line in file:
                coach_data = line.strip().split(',')
                if coach_data[0] == coach_id:
                    return coach_data
    except FileNotFoundError:
        print(f"File {COACHES_FILE} not found.")
    except Exception as e:
        print(f"An error occurred while finding coach: {str(e)}")
    return None

def display_coach_data(coach):
    fields = ["Coach ID", "Name", "Date Joined", "Date Terminated", "Hourly Rate", "Phone", "Address", "Sport Centre Code", "Sport Center Name", "Sport Code", "Sport Name", "Rating"]
    for i, field in enumerate(fields):
        print(f"{field}: {coach[i]}")
    print()

def search_student_by_id():
    target_student_id = input("Enter Student ID to search: ")
    try:
        found_student = None
        with open(REGISTERED_STUDENTS_FILE, "r") as file:
            for line in file:
                student_data = line.strip().split(',')
                if student_data[0] == target_student_id:
                    found_student = student_data
                    break

        if found_student:
            display_student_data(found_student)
        else:
            print(f"Student with ID {target_student_id} not found.")

    except FileNotFoundError:
        print("Registered students data file not found.")
    except Exception as e:
        print(f"An error occurred while searching student: {str(e)}")

def display_student_data(student):
    fields = ["Student ID", "Name", "Sport", "Coach", "Schedule"]
    for i, field in enumerate(fields):
        print(f"{field}: {student[i]}")
    print()
