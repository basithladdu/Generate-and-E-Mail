import pandas as pd
from datetime import datetime

# Read the Excel file
df = pd.read_excel('interns.csv', engine='openpyxl')
today_date = datetime.now().strftime("%d %B %Y")

# Process the data and print it
for index, row in df.iterrows():
    # Convert name to CamelCase
    full_name = row['FullName']
    camel_name = full_name.title()
    email = row['Email']
    print(f"Name: {camel_name}, Email: {email}, Date: {today_date}")