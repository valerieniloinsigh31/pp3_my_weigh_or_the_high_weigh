import gspread
from google.oauth2.service_account import Credentials
import math
from datetime import datetime
import os
from pprint import pprint 
import sys 

 

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('my_weigh_or_the_high_weigh')

""" 
FUNCTION 1: Using login and password from google sheets
"""
"""
FUNCTION 2: Collect latest weigh-in data from user
"""

def get_weighin_data(): 
    """
    Get the latest weigh-in values input for each of the six clients from the user. Must be kg (in numerical format and a float). Must have six values
    """
    while True:
        print ("Please enter the latest weigh-in data for your six clients (in kg)")
        print ("Must be to two decimal places, separated by commas, for each of the respective clients: Paul, John, James, Declan, Mike,Ian. ")
        print ("Last weigh-in: 82.70,87.45,97.32,103.9,83.45,76.55\n")

        latest_str = input("Enter latest weigh-in data here:\n")
        print(f"The latest weights provided for Paul, John, James, Declan, Mike and Ian were {latest_str}")

        weighin_data = latest_str.split(",")
        
        if validate_data(weighin_data):
            print("Weigh-in data provided!")
            break 

    return weighin_data 

def validate_data(values):
        print(values)
        """ 
        Inside the 'try: except:' error handling code, converts all strings into floats.
        Raises error if the string cannot be converted into a float or if there are not exactly 
        six values provided by the user.
        """
        try: 
            [float(value) for value in values]
            if len(values) != 6:
                raise ValueError (
                    f"Need to provide a value for each of the six clients, {len(values)} provided"
                )
        except ValueError as e:
            print(f"Invalid data: {e}, please submit again. ")
            return False

        return True 
"""
FUNCTION 3: Moving weigh-in data to the google sheets

"""
def update_weighin_worksheet(data):
    """ 
    Update week-end weigh-in worksheet, add new row with the values input by the user.
    """
    print ("Updating end-of-week weigh-in info for week 9...\n")
    weighin_worksheet = SHEET.worksheet("week_ends")
    weighin_worksheet.append_row(data)
    print ("Week 9 end-of-week weigh-in info updated successfully.\n")

data = get_weighin_data()
weighin_data = [float(num) for num in data]
update_weighin_worksheet(weighin_data)



