#username_password.py

import hash_passwords

def new_username_password():
  username = input("Please enter a username: ").capitalize()
  while True:
    symbols = ["?", "/", "<", ">", "(",")", '+', '-', "_", "%", "&"]
    print(f"""
      1. Passwords should be at minimum 7 characters long\n
      2. Passwords should contain a number\n
      3. Passwords should contain one of the following symbols: {symbols}\n""")
    password = input("Enter your password: ")
    if len(password) < 7:
      print("Passwords should be at minimum 7 characters long")
      continue
    if not any(char.isdigit() for char in password):
      print("Password should contain at least one number.")
      continue
    if not any(symbol in password for symbol in symbols):
      print(f"Password should contain at least one of the following symbols: {symbols}.")
      continue

    password = hash_passwords.hash_password(password)
    return username, password

    
