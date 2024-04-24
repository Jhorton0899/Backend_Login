#testing

import signup
import Login

def volunteer():
    while True:
        intro = input("Are you a new or returning volunteer (New/Returning), or press Q to quit? ").strip().capitalize()
        if intro == 'Q':
            print("Goodbye!")
            break
        elif intro.startswith('New'):
            print("We'll get you registered now.")
            signup.signup()  
            break
        elif intro.startswith('Returning'):
            print("Welcome back! Let's log you in.")
            Login.login()  
            break
        else:
            print("Sorry, that wasn't a valid response. Please try again.")
volunteer()
