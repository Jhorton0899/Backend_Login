#save

import pandas as pd
import pandas as pd

def save_to_excel(df):
    file_path = "C:\\Users\\vturn\\OneDrive\\pipeline\\volunteer_book.xlsx"
    sheet_name='Sheet1'
    try:
        with pd.ExcelWriter(file_path, engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
            try:
                existing_data = pd.read_excel(file_path, sheet_name=sheet_name)
                new_data = pd.concat([existing_data, df], ignore_index=True)
                new_data.to_excel(writer, sheet_name=sheet_name, index=False)
            except FileNotFoundError:
                df.to_excel(writer, sheet_name=sheet_name, index=False)
    except FileNotFoundError:
        df.to_excel(file_path, sheet_name=sheet_name, index=False)