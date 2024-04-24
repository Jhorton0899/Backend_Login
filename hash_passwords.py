#hash passwords
import hashlib 

def hash_password(password):
    hash_object = hashlib.sha256()
    hash_object.update(password.encode('utf-8'))
    return hash_object.hexdigest()

hashed_pw = hash_password('your_password_here')