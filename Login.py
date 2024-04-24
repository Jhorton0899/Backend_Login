#Login
import hash_passwords
import pandas as pd


def login_use(df, user_info):
    print("Logged in successfully.")
    df = df.drop(['password', 'locked', 'volunteer_id'], axis = 1)
    user_info = user_info[df.columns]  
    
    while True:
        for index, column in enumerate(df.columns, start=0):
            print(f"{index}: {column}")
        current_use_case = input("What would you like to access (Press Q to exit)? ").strip()
        if current_use_case.upper() == 'Q':
            print("Logout successful. Goodbye!")
            break
        
        
        try:
            column_index = int(current_use_case)
            if 0 <= column_index < len(df.columns):
                column_name = df.columns[column_index]
                print(f"{column_name}: {user_info.iloc[0, column_index]}")
            else:
                print("That column doesn't exist. Please try again.")
        except ValueError:
            print("Please enter a valid number or Q to exit.")

def login():
    df = pd.read_excel("C:\\Users\\vturn\\OneDrive\\pipeline\\volunteer_book.xlsx")
    max_attempts = 3
    for attempt in range(max_attempts):
        try:
            choice = input("Do you want to login using your username or volunteer ID? (username/ID): ").strip().lower()
            if choice not in ['username', 'id']:
                print("Please type 'username' or 'ID' to choose your login method.")
                continue
            
            if choice == 'username':
                username = input("Please enter your username: ").strip()
                user_match = df[df['username'] == username]
                if not user_match.empty:
                    current_user_password = user_match['password'].iloc[0]
                    user_password = input("Please enter your password: ").strip()
                    hashed_user_password = hash_passwords.hash_password(user_password)
                    if hashed_user_password == current_user_password:
                        print("Login successful!")
                        login_use(df, user_match)
                        return
                    else:
                        print("Incorrect password.")
                else:
                    print("Username not found.")
                    
            elif (choice == 'id') or (choice == 'ID'):
                id = input("Enter your ID: ")
                user_match = df[df['volunteer_id'] == id]
                if not user_match.empty:
                    print("Login successful")
                    login_use(df, user_match)
                    return
                else:
                    print("ID not found.")
                    
        except Exception as e:
            print(f"An error occurred: {e}")
            return
        print(f"Attempts left: {max_attempts - attempt - 1}")
    print("Maximum login attempts reached. Please contact support to reset your login.")