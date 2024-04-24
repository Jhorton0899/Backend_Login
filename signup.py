import username_password
import volunteer_id_generator
import name_address
import Contact
import pandas as pd
import save
import Login

def signup():
  name, city, state = name_address.get_name_address()
  username, password = username_password.new_username_password()
  volunteer_id = volunteer_id_generator.generate_volunteer_id()
  contact = Contact.get_contact()
  new_df = pd.DataFrame({
      'username':[username],
      'password':[password], 
      'volunteer_id': [volunteer_id],
      'name': [name], 
      'city': [city],
      'state':[state],
      'contact': [contact],
      'locked': [0]
      })
  save.save_to_excel(new_df)
  print(f"{name} this is your volunteer ID for later reference: {volunteer_id}")
  print(f"we'll reach out to you here {contact}")