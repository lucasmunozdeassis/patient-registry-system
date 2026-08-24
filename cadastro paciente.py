import json


print("Welcome to the patient registry system!")
print("Register Patient: 1\nConsult Registry: 2\nExit program:     3\nCheck Schedule:   4\nCheck Patients:   5\nDelete Patient:   6")   
option = int(input("What would you like to do?: "))
if option < 1 or option > 6:
    print("Invalid option. Please try again.")
    option = int(input("What would you like to do?: "))

try:
    with open("patients.json", "r") as file:
        patients = json.load(file)
except FileNotFoundError:
    patients = {}    

password = "none"


while option != 3:
    if option == 1:
        password_input = input("Enter password to register patient: ")
        attempts = 0
        while password_input != password and attempts < 2:
            print("Incorrect password. Please try again.")
            password_input = input("Enter password to register patient: ")
            attempts += 1
        if attempts == 2:
            print("Maximum number of attempts reached. Access denied.")
            reset = input("Do you want to restart the program? (y/n): ")
            if reset.lower() == "y":
                option = 1 
            elif reset.lower() == "n":
                print("Program finished.")
                break
            else:
                print("Invalid option. Program finished.")
                break
        if password_input != password:
            print("Register Patient: 1\nConsult Registry: 2\nExit program:     3\nCheck Schedule:   4\nCheck Patients:   5\nDelete Patient:   6")   
            option = int(input("What would you like to do?: "))
            if option < 1 or option > 6:
                print("Invalid option. Please try again.")
                option = int(input("What would you like to do?: "))
            if option == 3:
                print("Program finished.")
                break
            continue
            
        first_name = input("Enter patient's first name: ")
        if first_name == "" or first_name.isspace() or len(first_name) < 3 or len(first_name) > 50:
            print("Invalid name. Please try again.")
            continue
        last_name = input("Enter patient's last name: ")
        if last_name == "" or last_name.isspace() or not last_name.isalpha() or len(last_name) < 3 or len(last_name) > 50:
            print("Invalid last name. Please try again.")
            continue
        full_name = f"{first_name.strip().capitalize()} {last_name.strip().capitalize()}"
        if full_name in patients:
            print("Patient already registered.")
            continue
        
        patients[full_name.strip().capitalize()] = {}


        age = int(input("Enter patient's age: "))
        if age <= 0:
            print("Invalid age. Please try again.")
            continue
        id_number = input("Enter patient's CPF/ID: ")
        if id_number == "" or id_number.isspace():
            print("Invalid CPF/ID. Please try again.")
            continue
        patients[full_name.strip().capitalize()]['age'] = age
        patients[full_name.strip().capitalize()]['id_number'] = id_number
        history = input("Enter patient's history: ")
        if history == "" or history.isspace():
            print("Invalid history. Please try again.")
            continue
        history = patients[full_name.strip().capitalize()]['history'] = history
        appointment = input("Enter appointment date (dd/mm/yyyy): ")
        if appointment == "" or appointment.isspace() or len(appointment) != 10 or appointment[2] != '/' or appointment[5] != '/':
            print("Invalid appointment date. Please try again.")
            continue
        elif appointment[0:2].isdigit() == False or appointment[3:5].isdigit() == False or appointment[6:10].isdigit() == False:
            print("Invalid appointment date. Please try again.")
            continue
        else:
            day = int(appointment[0:2])
            month = int(appointment[3:5])
            year = int(appointment[6:10])
            if day < 1 or day > 31 or month < 1 or month > 12 or year < 1900:
                print("Invalid appointment date. Please try again.")
                continue
        time_slot = input("Enter appointment time (hh:mm): ")
        if time_slot == "" or time_slot.isspace() or len(time_slot) != 5 or time_slot[2] != ':':
            print("Invalid appointment time. Please try again.")
            continue
        elif time_slot[0:2].isdigit() == False or time_slot[3:5].isdigit() == False:
            print("Invalid appointment time. Please try again.")
            continue
        else:
            hour = int(time_slot[0:2])
            minute = int(time_slot[3:5])
            if hour < 0 or hour > 23 or minute < 0 or minute > 59:
                print("Invalid appointment time. Please try again.")
                continue
        appointment = patients[full_name.strip().capitalize()]['appointment'] = f"{appointment} {time_slot}"
        
        appointment = patients[full_name.strip().capitalize()]['appointment'] = appointment

        print(f"Patient {full_name} registered successfully!")
        with open("patients.json", "w") as file:
            json.dump(patients, file)    
    elif option == 2:
        password_input = input("Enter password to consult patient: ")
        attempts = 0
        while password_input != password and attempts < 2:
            print("Incorrect password. Please try again.")
            password_input = input("Enter password to consult patient: ")
            attempts += 1
        if attempts == 2:
            print("Maximum number of attempts reached. Access denied.")
            reset = input("Do you want to restart the program? (y/n): ")
            if reset.lower() == "y":
                option = 1 
            elif reset.lower() == "n":
                print("Program finished.")
                break
            else:
                print("Invalid option. Program finished.")
                break
        if password_input != password:
            print("Register Patient: 1\nConsult Registry: 2\nExit program:     3\nCheck Schedule:   4\nCheck Patients:   5\nDelete Patient:   6")   
            option = int(input("What would you like to do?: "))
            if option < 1 or option > 6:
                print("Invalid option. Please try again.")
                option = int(input("What would you like to do?: "))
            if option == 3:
                print("Program finished.")
                break
            continue

        search_name = input("Enter the name of the patient you want to consult: ")
        if search_name in patients and patients[search_name]['age'] is not None and patients[search_name]['id_number'] is not None and patients[search_name]['history'] is not None and patients[search_name]['appointment'] is not None:
            search_name = search_name.strip().capitalize()
            age = patients[search_name]['age']
            id_number = patients[search_name]['id_number']
            history = patients[search_name]['history']
            appointment = patients[search_name]['appointment']
            print(f"Name: {search_name}, Age: {age}, CPF/ID: {id_number}, History: {history}, Appointment: {appointment}")
        elif search_name in patients and (patients[search_name]['age'] is None or patients[search_name]['id_number'] is None or patients[search_name]['history'] is None or patients[search_name]['appointment'] is None):
            print(f"Patient {search_name} does not have all information registered.")
        elif search_name not in patients:
            print("Patient not found.")


    elif option == 4:
        password_input = input("Enter password to access schedule: ")
        attempts = 0
        while password_input != password and attempts < 2:
            print("Incorrect password. Please try again.")
            password_input = input("Enter password to access schedule: ")
            attempts += 1
        if attempts == 2:
            print("Maximum number of attempts reached. Access denied.")
            reset = input("Do you want to restart the program? (y/n): ")
            if reset.lower() == "y":
                option = 1 
            elif reset.lower() == "n":
                print("Program finished.")
                break
            else:
                print("Invalid option. Program finished.")
                break
        if password_input != password:
            print("Register Patient: 1\nConsult Registry: 2\nExit program:     3\nCheck Schedule:   4\nCheck Patients:   5\nDelete Patient:   6")   
            option = int(input("What would you like to do?: "))
            if option < 1 or option > 6:
                print("Invalid option. Please try again.")
                option = int(input("What would you like to do?: "))
            if option == 3:
                print("Program finished.")
                break
            continue
        if not patients:
            print("No patients registered.")
        else:
            print("Patient Schedule:")
            for name, info in patients.items():
                print(f"Name: {name}, Appointment: {info['appointment']}")
    elif option == 5:
        attempts = 0
        password_input = input("Enter password to access patients list: ")
        while password_input != password and attempts < 2:
            print("Incorrect password. Please try again.")
            password_input = input("Enter password to access patients list: ")
            attempts += 1
        if attempts == 2:
            print("Maximum number of attempts reached. Access denied.")
            reset = input("Do you want to restart the program? (y/n): ")
            if reset.lower() == "y":
                option = 1 
            elif reset.lower() == "n":
                print("Program finished.")
                break
            else:
                print("Invalid option. Program finished.")
                break
        if password_input == password:
            if not patients:
                print("No patients registered.")
            else:
                print("Patient List:")
                for name, info in patients.items():
                    print(f"Name: {name.strip().capitalize()}, Age: {info['age']}, CPF/ID: {info['id_number']}, History: {info['history']}, Appointment: {info['appointment']}")
    elif option == 6:
        password_input = input("Enter password to delete patient: ")
        attempts = 0
        while password_input != password and attempts < 2:
            print("Incorrect password. Please try again.")
            password_input = input("Enter password to delete patient: ")
            attempts += 1
        if attempts == 2:
            print("Maximum number of attempts reached. Access denied.")
            reset = input("Do you want to restart the program? (y/n): ")
            if reset.lower() == "y":
                option = 1 
            elif reset.lower() == "n":
                print("Program finished.")
                break
            else:
                print("Invalid option. Program finished.")
                break
        if password_input != password:
            print("Register Patient: 1\nConsult Registry: 2\nExit program:     3\nCheck Schedule:   4\nCheck Patients:   5\nDelete Patient:   6")   
            option = int(input("What would you like to do?: "))
            if option < 1 or option > 6:
                print("Invalid option. Please try again.")
                option = int(input("What would you like to do?: "))
            if option == 3:
                print("Program finished.")
                break
            continue
        if not patients:
            print("No patients registered.")
        else:
            delete_name = input("Enter the name of the patient you want to delete: ")
            if delete_name in patients:
                del patients[delete_name]
                print(f"Patient {delete_name} deleted successfully!")
            else:
                print("Patient not found.")
        with open("patients.json", "w") as file:
            json.dump(patients, file)
    else:
        print("Invalid option. Please try again.")
    
    
    print("\nRegister Patient: 1\nConsult Registry: 2\nExit program:     3\nCheck Schedule:   4\nCheck Patients:   5\nDelete Patient:   6   ")   
    option = int(input("What would you like to do?: "))