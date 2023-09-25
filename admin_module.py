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

        elif choice == "2":
            while True:
                print("\nDisplay Menu:")
                print("1. Display All Coaches")
                print("2. Display All Sports")
                print("3. Display Registered Students")
                print("4. Back")

                sub_choice = input("Enter your choice: ")

                if sub_choice == "1":
                    print()
                    display_all_coaches()
                elif sub_choice == "2":
                    print()
                    display_all_sports()
                elif sub_choice == "3":
                    print()
                    display_registered_students()
                elif sub_choice == "4":
                    break
                else:
                    print("Invalid choice. Please try again.")

        elif choice == "3":
            while True:
                print("\nSearch Menu:")
                print("1. Search Coach")
                print("2. Search Sport")
                print("3. Search Student")
                print("4. Back")

                sub_choice = input("Enter your choice: ")

                if sub_choice == "1":
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

                elif sub_choice == "2":
                    sport_id = input("Enter Sport ID to search: ")
                    search_sport_by_id(sport_id)
                elif sub_choice == "3":
                    student_id = input("Enter Student ID to search: ")
                    search_student_by_id(student_id)
                elif sub_choice == "4":
                    break
                else:
                    print("Invalid choice. Please try again.")

        elif choice == "4":
            while True:
                print("\nModify Menu:")
                print("1. Modify Coach")
                print("2. Modify Sport")
                print("3. Modify Sport Schedule")
                print("4. Back")

                sub_choice = input("Enter your choice: ")

                if sub_choice == "1":
                    coach_id = input("Enter Coach ID to modify: ")
                    modify_coach_by_id(coach_id)
                elif sub_choice == "2":
                    sport_id = input("Enter Sport ID to modify: ")
                    modify_sport_by_id(sport_id)
                elif sub_choice == "3":
                    modify_sport_schedule()
                elif sub_choice == "4":
                    break
                else:
                    print("Invalid choice. Please try again.")

        elif choice == "5":
            return "exit"
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
        pass  # If the file doesn't exist, there are no duplicates
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
    date_terminated = input(
        "Enter Date Terminated (leave empty if not terminated): ")
    hourly_rate = input("Enter Hourly Rate: ")
    phone = input("Enter Phone: ")
    address = input("Enter Address: ")
    sport_centre_code = input("Enter Sport Centre Code: ")
    sport_center_name = input("Enter Sport Center Name: ")
    sport_code = input("Enter Sport Code: ")
    sport_name = input("Enter Sport Name: ")
    rating = input("Enter Rating (1 to 5): ")

    try:
        with open(COACHES_FILE, "a") as file:
            coach_data = ",".join([coach_id, name, date_joined, date_terminated or 'N/A', hourly_rate,
                                  phone, address, sport_centre_code, sport_center_name, sport_code, sport_name, rating])
            file.write(coach_data + "\n")

        print("Coach added successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def check_duplicate_sport_id(sport_id):
    try:
        with open(SPORTS_FILE, "r") as file:
            for line in file:
                existing_sport_id, *_ = line.strip().split(',')
                if existing_sport_id == sport_id:
                    return True
    except FileNotFoundError:
        pass  # If the file doesn't exist, there are no duplicates
    return False


def add_sport():
    while True:
        sport_id = input("Enter Sport ID: ")
        if check_duplicate_sport_id(sport_id):
            print("Sport with this ID already exists. Please enter a unique Sport ID.")
        else:
            break

    sport_name = input("Enter Sport Name: ")

    try:
        with open(SPORTS_FILE, "a") as file:
            sport_data = f"{sport_id},{sport_name}"
            file.write(sport_data + "\n")

        print("Sport added successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def add_sport_schedule():
    try:
        print("Please enter schedule information:")
        sport_schedule_id = input("Sport Schedule ID: ")
        sport_centre = input("Sport Centre: ")
        coach_id = input("Coach ID: ")
        day = input("Day (e.g., Monday): ")
        time = input("Time (e.g., 10:00 AM): ")

        # Compose the schedule data as a string
        schedule_data = f"{sport_schedule_id},{sport_centre},{coach_id},{day},{time}"

        # Write the schedule data to the file
        with open(SCHEDULE_FILE, "a") as file:
            file.write(schedule_data + "\n")

        print("Sport Schedule added successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def display_all_coaches():
    try:
        with open(COACHES_FILE, "r") as file:
            next(file)  # Skip the first line (header)
            for line in file:
                coach_data = line.strip().split(',')
                coach_id, name, date_joined, date_terminated, hourly_rate, phone, address, sport_centre_code, sport_center_name, sport_code, sport_name, rating = coach_data
                print(f"Coach ID: {coach_id}")
                print(f"Name: {name}")
                print(f"Date Joined: {date_joined}")
                print(
                    f"Date Terminated: {date_terminated if date_terminated else 'N/A'}")
                print(f"Hourly Rate: {hourly_rate}")
                print(f"Phone: {phone}")
                print(f"Address: {address}")
                print(f"Sport Centre Code: {sport_centre_code}")
                print(f"Sport Center Name: {sport_center_name}")
                print(f"Sport Code: {sport_code}")
                print(f"Sport Name: {sport_name}")
                print(f"Rating: {rating}")
                print()  # Add an empty line for separation
    except FileNotFoundError:
        print("Coaches data file not found.")


def display_all_sports():
    try:
        with open(SPORTS_FILE, "r") as file:
            next(file)  # Skip the first line (header)
            for line in file:
                sport_data = line.strip().split(',')
                sport_id, sport_name = sport_data
                print(f"Sport ID: {sport_id}")
                print(f"Sport Name: {sport_name}")
                print()  # Add an empty line for separation
    except FileNotFoundError:
        print("Sports data file not found.")


def display_registered_students():
    try:
        with open(REGISTERED_STUDENTS_FILE, "r") as file:
            for line in file:
                student_data = line.strip().split(',')
                if len(student_data) == 6:
                    student_id, name, sport, coach, schedule, password = student_data
                    print(f"Student ID: {student_id}")
                    print(f"Name: {name}")
                    print(f"Sport: {sport}")
                    print(f"Coach: {coach}")
                    print(f"Schedule: {schedule}")
                    print()  # Add an empty line for separation
                else:
                    print("Invalid data format in the file.")
    except FileNotFoundError:
        print("Registered students data file not found.")


def modify_coach_by_id(target_coach_id):
    try:
        coach_data_list = []  # To store updated coach data
        found = False

        # Read all coach data from the file and update the specific coach data
        with open(COACHES_FILE, "r") as file:
            for line in file:
                coach_data = line.strip().split(',')
                coach_id = coach_data[0]

                if coach_id == target_coach_id:
                    found = True
                    # Display the existing data for reference
                    print(f"Current Coach Data for ID {target_coach_id}:")
                    print("Coach ID:", coach_data[0])
                    print("Name:", coach_data[1])
                    print("Date Joined:", coach_data[2])
                    print("Date Terminated:", coach_data[3])
                    print("Hourly Rate:", coach_data[4])
                    print("Phone:", coach_data[5])
                    print("Address:", coach_data[6])
                    print("Sport Centre Code:", coach_data[7])
                    print("Sport Center Name:", coach_data[8])
                    print("Sport Code:", coach_data[9])
                    print("Sport Name:", coach_data[10])
                    print("Rating:", coach_data[11])
                    print()

                    # Prompt for updated data
                    name = input(
                        f"Enter updated Name (press Enter to keep existing, current: {coach_data[1]}): ")
                    date_joined = input(
                        f"Enter updated Date Joined (press Enter to keep existing, current: {coach_data[2]}): ")
                    date_terminated = input(
                        f"Enter updated Date Terminated (press Enter to keep existing, current: {coach_data[3]}): ")
                    hourly_rate = input(
                        f"Enter updated Hourly Rate (press Enter to keep existing, current: {coach_data[4]}): ")
                    phone = input(
                        f"Enter updated Phone (press Enter to keep existing, current: {coach_data[5]}): ")
                    address = input(
                        f"Enter updated Address (press Enter to keep existing, current: {coach_data[6]}): ")
                    sport_centre_code = input(
                        f"Enter updated Sport Centre Code (press Enter to keep existing, current: {coach_data[7]}): ")
                    sport_center_name = input(
                        f"Enter updated Sport Center Name (press Enter to keep existing, current: {coach_data[8]}): ")
                    sport_code = input(
                        f"Enter updated Sport Code (press Enter to keep existing, current: {coach_data[9]}): ")
                    sport_name = input(
                        f"Enter updated Sport Name (press Enter to keep existing, current: {coach_data[10]}): ")
                    rating = input(
                        f"Enter updated Rating (1 to 5, press Enter to keep existing, current: {coach_data[11]}): ")

                    # Update the coach data
                    updated_coach_data = [
                        coach_id,
                        name if name else coach_data[1],
                        date_joined if date_joined else coach_data[2],
                        date_terminated if date_terminated else coach_data[3],
                        hourly_rate if hourly_rate else coach_data[4],
                        phone if phone else coach_data[5],
                        address if address else coach_data[6],
                        sport_centre_code if sport_centre_code else coach_data[7],
                        sport_center_name if sport_center_name else coach_data[8],
                        sport_code if sport_code else coach_data[9],
                        sport_name if sport_name else coach_data[10],
                        rating if rating else coach_data[11]
                    ]
                    coach_data_list.append(updated_coach_data)
                else:
                    coach_data_list.append(coach_data)

        if not found:
            print(f"Coach with ID {target_coach_id} not found.")

        # Write the updated coach data back to the file
        with open(COACHES_FILE, "w") as file:
            for coach_data in coach_data_list:
                file.write(','.join(coach_data) + '\n')

        if found:
            print(f"Coach with ID {target_coach_id} updated successfully.")

    except FileNotFoundError:
        print("Coaches data file not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def modify_sport_by_id(target_sport_id):
    try:
        sport_data_list = []  # To store updated sport data
        found = False

        # Read all sport data from the file and update the specific sport data
        with open(SPORTS_FILE, "r") as file:
            for line in file:
                sport_data = line.strip().split(',')
                sport_id = sport_data[0]

                if sport_id == target_sport_id:
                    found = True
                    # Display the existing data for reference
                    print(f"Current Sport Data for ID {target_sport_id}:")
                    print("Sport ID:", sport_data[0])
                    print("Sport Name:", sport_data[1])
                    print()

                    # Prompt for updated data
                    sport_name = input(
                        "Enter updated Sport Name (press Enter to keep existing): ")

                    # Update the sport data
                    updated_sport_data = [sport_id, sport_name]
                    sport_data_list.append(updated_sport_data)
                else:
                    sport_data_list.append(sport_data)

        if not found:
            print(f"Sport with ID {target_sport_id} not found.")

        # Write the updated sport data back to the file
        with open(SPORTS_FILE, "w") as file:
            for sport_data in sport_data_list:
                file.write(','.join(sport_data) + '\n')

        if found:
            print(f"Sport with ID {target_sport_id} updated successfully.")

    except FileNotFoundError:
        print("Sports data file not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def modify_sport_schedule():
    try:
        schedule_id = input("Enter the Sport Schedule ID to modify: ")
        found_schedule = None
        updated_schedules = []

        with open(SCHEDULE_FILE, "r") as file:
            for line in file:
                schedule_data = line.strip().split(',')
                if schedule_data[0] == schedule_id:
                    found_schedule = schedule_data
                    updated_schedule = []

                    # Prompt for updated schedule fields
                    for field, value in zip(schedule_data, found_schedule):
                        updated_value = input(
                            f"Enter updated {field} (press Enter to keep existing): ")
                        updated_schedule.append(
                            updated_value if updated_value else value)

                    updated_schedules.append(updated_schedule)
                else:
                    updated_schedules.append(schedule_data)

        if found_schedule:
            with open(SCHEDULE_FILE, "w") as file:
                for updated_schedule_data in updated_schedules:
                    updated_schedule_line = ','.join(updated_schedule_data)
                    file.write(updated_schedule_line + "\n")

            print(f"Sport Schedule with ID {schedule_id} has been updated.")
        else:
            print(f"Sport Schedule with ID {schedule_id} not found.")

    except FileNotFoundError:
        print("Sport Schedules data file not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def search_sport_by_id(target_sport_id):
    try:
        with open(SPORTS_FILE, "r") as file:
            next(file)  # Skip the first line (header)
            for line in file:
                sport_id, sport_name = line.strip().split(',')
                if sport_id == target_sport_id:
                    print()
                    print("Sport ID:", sport_id)
                    print("Sport Name:", sport_name)
                    return  # Exit the function after finding the sport

        print(f"Sport with ID {target_sport_id} not found.")

    except FileNotFoundError:
        print("Sports data file not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def search_coach_by_rating():
    try:
        target_rating = input(
            "Enter the rating (1 to 5) to search for coaches: ")
        found_coaches = []

        with open(COACHES_FILE, "r") as file:
            next(file)  # Skip the first line (header)
            for line in file:
                coach_data = line.strip().split(',')
                rating = coach_data[-1]

                if rating == target_rating:
                    found_coaches.append(coach_data)

        if found_coaches:
            print(f"Coaches with rating {target_rating}:")
            for coach in found_coaches:
                print()
                display_coach_data(coach)
                print()  # Add an empty line for separation
        else:
            print(f"No coaches found with rating {target_rating}.")

    except FileNotFoundError:
        print("Coaches data file not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def search_coach_by_id(coach_id):
    try:
        found_coach = find_coach_by_id(coach_id)

        if found_coach:
            display_coach_data(found_coach)
        else:
            print(f"Coach with ID {coach_id} not found.")

    except FileNotFoundError:
        print("Coaches data file not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def find_coach_by_id(coach_id):
    with open(COACHES_FILE, "r") as file:
        for line in file:
            coach_data = line.strip().split(',')
            if coach_data[0] == coach_id:
                return coach_data
    return None


def display_coach_data(coach):
    print("Coach ID:", coach[0])
    print("Name:", coach[1])
    print("Date Joined:", coach[2])
    print("Date Terminated:", coach[3])
    print("Hourly Rate:", coach[4])
    print("Phone:", coach[5])
    print("Address:", coach[6])
    print("Sport Centre Code:", coach[7])
    print("Sport Center Name:", coach[8])
    print("Sport Code:", coach[9])
    print("Sport Name:", coach[10])
    print("Rating:", coach[11])


def search_student_by_id(target_student_id):
    try:
        found_student = None

        with open(REGISTERED_STUDENTS_FILE, "r") as file:
            next(file)  # Skip the first line (header)
            for line in file:
                student_data = line.strip().split(',')
                student_id, name, sport, coach, schedule, _ = student_data

                if student_id == target_student_id:
                    found_student = student_data
                    break  # Exit the loop after finding the student

        if found_student:
            print()
            display_student_data(found_student)
        else:
            print(f"Student with ID {target_student_id} not found.")

    except FileNotFoundError:
        print("Registered students data file not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def display_student_data(student):
    print("Student ID:", student[0])
    print("Name:", student[1])
    print("Sport:", student[2])
    print("Coach:", student[3])
    print("Schedule:", student[4])
