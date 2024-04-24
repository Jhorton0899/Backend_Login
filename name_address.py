#name_address
import requests

def fetch_location():
    try:
        response = requests.get('http://ipinfo.io/json')
        data = response.json()
        city = data.get('city', 'City not found')
        state = data.get('region', 'Region not found')
        return city, state
    except requests.RequestException:
        return 'City not found', 'Region not found'

def get_name_address():
    while True:
        name = input("Enter your name: ").strip()
        if name.replace(" ", "").isalpha():
            break
        else:
            print("Please enter a name without symbols or numbers.")
    yes = ['yes', 'yeah', 'y']
    location_permission = input("Can we use your current location to find volunteer opportunities near you? (Yes/No) ").lower()
    if any(word in location_permission for word in yes):
        city, state = fetch_location()
        correct = input(f"Does this seem right? {city}, {state} (Yes/No) ").lower()
        if any(word in correct for word in yes):
            return (name.capitalize(), city.capitalize(), state.capitalize())
        else:
            print("Let's try fetching your location again or enter it manually.")
    state = input("Please enter your state: ").strip()
    city = input("Please enter your city: ").strip()
    return (name.capitalize(), city, state)
