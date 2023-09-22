import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd


# Connect to Google
# Scope: Enable access to specific links
scope = ['https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name("D:\Code\gym log\gscredentials.json", scope)

client = gspread.authorize(credentials)

# Open the Google Sheet
sheet = client.open('Gym')

worksheet = sheet.get_worksheet(0)  # Assuming you want to work with the first worksheet

data = worksheet.get_all_values()

#names = [row[0] for row in data[1:]]  # Assuming first row contains headers

filtered_rows = [row for row in data[1:] if int(row[1]) > 10]  # Assuming the first row contains headers

specific_values = [row[0] for row in filtered_rows]  # Assuming the first column contains the values you want


# Create a blank spreadsheet (Note: We're using a service account, so this spreadsheet is visible only to this account)
#sheet = client.create("NewDatabase")

# To access newly created spreadsheet from Google Sheets with your own Google account you must share it with your email
# Sharing a Spreadsheet
#sheet.share('sdimov77@gmail.com', perm_type='user', role='writer')

# Open the spreadsheet
#sheet = client.open("NewDatabase").sheet1
# read csv with pandas
#df = pd.read_csv('D:\Code\gym log\\football_news.csv')
# export df to a sheet
#sheet.update([df.columns.values.tolist()] + df.values.tolist())

#https://docs.google.com/spreadsheets/d/1CxCLvg2CGSHYNWskSa8JlBOPmF4th4XPEQQfy6AouYw/edit?usp=sharing