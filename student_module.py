import os

# File paths
COACHES_FILE = "files/coaches.txt"
SPORTS_FILE = "files/sports.txt"
SCHEDULE_FILE = "files/sport_schedule.txt"
REGISTERED_STUDENTS_FILE = "files/registered_students.txt"
FEEDBACK_FILE = "files/feedback.txt"

def registered_student_menu(student_id):
    while True:
        print("\nRegistered Student Menu:")
        print("1. View Coach Details")
        print("2. View Self-Record")
        print("3. Modify Self-Record")
        print("4. Provide Feedback and Star Ratings to Coaches")
        print("5. View Registered Sport Schedule")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_coach_details()
        elif choice == "2":
            view_self_record(student_id)
        elif choice == "3":
            modify_self_record(student_id)
        elif choice == "4":
            provide_feedback_and_ratings(student_id)
        elif choice == "5":
            view_registered_sport_schedule(student_id)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

def student_menu():
    student_id = None
    while True:
        print("\nStudent Menu:")
        print("1. View Sport Details")
        print("2. View Sport Schedule")
        print("3. Login")
        print("4. Register")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_sport_details()
        elif choice == "2":
            view_all_sport_schedules()
        elif choice == "3":
            student_id = login_student()
            if student_id is not None:
                registered_student_menu(student_id)
                break
        elif choice == "4":
            register_student()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

def login_student():
    registered_students = read_data(REGISTERED_STUDENTS_FILE)

    while True:
        student_id = input("Enter Student ID: ").strip()
        password = input("Enter Password: ").strip()

        if not student_id or not password:
            print("Student ID and password cannot be empty. Please try again.")
            continue

        for student in registered_students:
            data = student.strip().split(',')
            if data[0] == student_id and data[-1] == password:
                print("Login Successful!")
                return student_id

        print("Invalid ID or password. Please try again.")

def read_data(file_path):
    try:
        with open(file_path, "r") as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"File {file_path} not found.")
    except Exception as e:
        print(f"An error occurred while reading data: {str(e)}")
    return []

def register_student():
    registered_students = read_data(REGISTERED_STUDENTS_FILE)
    new_student_id = input("Enter a new Student ID: ").strip()

    if any(student.startswith(new_student_id + ',') for student in registered_students):
        print("Student ID already exists. Please choose another.")
        return

    new_name = input("Enter Name: ").strip()
    new_sport = input("Enter Sport: ").strip()
    new_coach = input("Enter Coach: ").strip()
    new_schedule = input("Enter Schedule: ").strip()
    new_password = input("Create a Password: ").strip()

    registration_data = f"{new_student_id},{new_name},{new_sport},{new_coach},{new_schedule},{new_password}"
    try:
        with open(REGISTERED_STUDENTS_FILE, "a") as file:
            file.write(registration_data + "\n")
        print("Registration Successful!")
    except Exception as e:
        print(f"An error occurred while saving registration data: {str(e)}")

def provide_feedback_and_ratings(student_id):
    coach_id = input("Enter Coach ID you want to provide feedback for: ").strip()
    feedback = input("Enter your feedback for the coach: ").strip()

    coaches = read_data(COACHES_FILE)
    valid_coach_ids = [coach.split(',')[0] for coach in coaches]
    if coach_id not in valid_coach_ids:
        print("Invalid Coach ID. Please enter a valid Coach ID.")
        return

    rating = input("Enter a star rating (1-5) for the coach: ").strip()

    try:
        rating = int(rating)
        if rating < 1 or rating > 5:
            print("Invalid rating. Please enter a rating between 1 and 5.")
            return
    except ValueError:
        print("Invalid rating. Please enter a numeric rating between 1 and 5.")
        return

    try:
        with open(FEEDBACK_FILE, "a") as file:
            file.write(f"{student_id},{coach_id},{feedback},{rating}\n")
        print("Feedback and rating submitted successfully!")
    except Exception as e:
        print(f"An error occurred while saving feedback: {str(e)}")

def view_coach_details():
    try:
        with open(COACHES_FILE, "r") as file:
            next(file)
            for line in file:
                coach_data = line.strip().split(',')
                coach_id, name, date_joined, date_terminated, hourly_rate, phone, address, sport_centre_code, sport_center_name, sport_code, sport_name, rating = coach_data
                print(f"Coach ID: {coach_id}")
                print(f"Name: {name}")
                print(f"Date Joined: {date_joined}")
                print(f"Date Terminated: {date_terminated if date_terminated else 'N/A'}")
                print(f"Hourly Rate: {hourly_rate}")
                print(f"Phone: {phone}")
                print(f"Address: {address}")
                print(f"Sport Centre Code: {sport_centre_code}")
                print(f"Sport Center Name: {sport_center_name}")
                print(f"Sport Code: {sport_code}")
                print(f"Sport Name: {sport_name}")
                print(f"Rating: {rating}\n")
    except FileNotFoundError:
        print("Coaches data file not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def view_sport_details():
    sports = read_data(SPORTS_FILE)
    print("\nSport Details:")
    for sport in sports:
        sport_id, sport_name = sport.strip().split(',')
        print(f"Sport ID: {sport_id}")
        print(f"Sport Name: {sport_name}\n")

def view_registered_sport_schedule(student_id):
    registered_students = read_data(REGISTERED_STUDENTS_FILE)

    for student in registered_students:
        data = student.strip().split(',')
        if data[0] == student_id:
            print(f"\nYour Sport Schedule: {data[4]}")
            return

    print("Student not found or schedule not available.")

def view_self_record(student_id):
    registered_students = read_data(REGISTERED_STUDENTS_FILE)

    for student in registered_students:
        data = student.strip().split(',')
        if data[0] == student_id:
            print("\nYour Registration Details:")
            print(f"Student ID: {data[0]}")
            print(f"Name: {data[1]}")
            print(f"Sport: {data[2]}")
            print(f"Coach: {data[3]}")
            print(f"Schedule: {data[4]}")
            return

    print("Student not found. Please try again later.")

def modify_self_record(student_id):
    registered_students = read_data(REGISTERED_STUDENTS_FILE)
    modified_students = []

    for student in registered_students:
        data = student.strip().split(',')
        if data[0] == student_id:
            print("\nYour Current Registration Details:")
            print(f"Student ID: {data[0]}")
            print(f"Name: {data[1]}")
            print(f"Sport: {data[2]}")
            print(f"Coach: {data[3]}")
            print(f"Schedule: {data[4]}")

            name = input("Enter updated Name (press Enter to keep existing): ")
            sport = input("Enter updated Sport (press Enter to keep existing): ")
            coach = input("Enter updated Coach (press Enter to keep existing): ")
            schedule = input("Enter updated Schedule (press Enter to keep existing): ")

            data[1] = name if name else data[1]
            data[2] = sport if sport else data[2]
            data[3] = coach if coach else data[3]
            data[4] = schedule if schedule else data[4]

        modified_students.append(','.join(data))

    try:
        with open(REGISTERED_STUDENTS_FILE, "w") as file:
            file.writelines('\n'.join(modified_students))
        print("Your registration details have been updated.")
    except Exception as e:
        print(f"An error occurred while saving modifications: {str(e)}")

def view_all_sport_schedules():
    sport_schedules = read_data(SCHEDULE_FILE)
    if sport_schedules:
        print("\nAll Sport Schedules:")
        for schedule in sport_schedules:
            print(schedule.strip())
    else:
        print("No sport schedules available.")
