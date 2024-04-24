#Contact 
import re

def get_contact():
    contact = input("Please enter your email address or a phone number for best form of contact: ").strip()
    email_pattern = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
    phone_pattern = re.compile(r"^(\+\d{1,2}\s?)?(\(\d{3}\)|\d{3})[\s.-]?\d{3}[\s.-]?\d{4}$")

    if email_pattern.match(contact):
        print("Email Address Validated.")
        return contact
    elif phone_pattern.match(contact):
        print("Phone Number Validated.")
        return contact
    else:
        print("Invalid input. Please enter a valid email address or phone number.")
        return None

