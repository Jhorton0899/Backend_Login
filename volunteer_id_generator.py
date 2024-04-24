# volunteer_id_generator.py
import uuid

def generate_volunteer_id():
    long_id = str(uuid.uuid4())  # Generate a UUID formatted string
    short_id = long_id[:8]  # Take the first 8 characters to shorten it
    return(short_id)