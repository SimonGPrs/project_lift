import csv
import os

def main():

    while True:  # Entry point to log in or create account
        account = input("Do you have an account? (yes/no): ").strip().lower()
        if account == "yes":
            log_in()
            break
        elif account == "no":
            create()
            break
        else:
            print("Invalid input. Please answer by 'yes' or 'no'.")
    


def log_in():
    user = input("User: ")
    password = input("Password: ")
    file_path = r"C:\Users\simon\OneDrive\Desktop\project_lift\Lift.csv"

    try:
        with open(file_path, mode="r", encoding="utf-8-sig", newline="") as file:
            csv_reader = csv.reader(file)
            header = next(csv_reader)
            print(f"CSV Header: {header}") #Debug
            
            user_col_index = header.index("user")
            password_col_index = header.index("password")

            for row in csv_reader:
                print(f"check row: {row}")
                if row[user_col_index] == user and row[password_col_index] == password:
                    print("Logged in successfully.")
                    return check_first_session()
                else:
                    print("Invalid username or password")
    except FileNotFoundError:
        print(f"File {file_path} not found")

   

def create(): # create an account
    print("Welcome to the sign-up page!")
    name = input("Enter your full name: ")
    mail = input("Mail: ")
    password = input("Create a password: ")
    user_info(name, mail, password)


def user_info(name, mail, password):
    f_name = input("First name: ")
    l_name = input("Last name: ")
    gender = input("What do you identify as? ")
    birthdate = input("Birthday (YYYY-MM-DD): ")
    
    # Save user data to CSV
    with open("user.csv", mode="a", newline='') as file:  # Append to the CSV file
        writer = csv.writer(file)
        writer.writerow([f_name, l_name, gender, birthdate, name, mail, password])

    print("Account created successfully.")
    first_session()



def check_first_session():
    file_path = r"C:\Users\simon\OneDrive\Desktop\project_lift\Lift.csv"
    session_found = False

    try:
        with open(file_path, mode="r", encoding="utf-8-sig", newline="") as file:
            csv_reader = csv.reader(file)
            header = next(csv_reader)
            print(f"CSV Header: {header}")  # Debug

            session_number_col_index = header.index("session_number")
            
            for row in csv_reader:
                print(f"check row: {row}")  # Debug
                if row[session_number_col_index].strip() == "1":  # Check if session number is "1"
                    session_found = True
                    break

            if session_found:
                
                return new_session()  # Call function for existing session
            else:
                
                return first_session()  # Call function for first session

    except FileNotFoundError:
        print(f"File {file_path} not found")
        return None




def first_session():
    # Placeholder for first session actions
    print("Welcome to your first session!")
    new_session()


def new_session():
    feeling = input("How do you feel today? (very good/good/ok/bad): ").lower()
    
    # Placeholder values for demonstration
    weight1, weight2, weight3 = 50, 50, 50  # Replace with actual logic to retrieve weights
    rep1, rep2, rep3 = 10, 10, 10  # Replace with actual logic to retrieve reps

    objective = None
    
    if feeling == "very good" and weight1 == weight2 == weight3 and rep1 == rep2 == rep3:
        objective = weight1 + 5 
    elif feeling == "good" and weight1 == weight2 == weight3 and rep1 == rep2 == rep3:
        objective = weight1 + 1.5
    elif feeling == "ok" and weight1 == weight2 == weight3 and rep1 == rep2 == rep3:
        objective = weight1
    elif feeling == "bad" and weight1 == weight2 == weight3 and rep1 == rep2 == rep3:
        objective = weight1 - 1.5
    else:
        print("Invalid input or condition.")

    print(f"Your new objective is: {objective} kg")

if __name__ == "__main__":
    main()


    
