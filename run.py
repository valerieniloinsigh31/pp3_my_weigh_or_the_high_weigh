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
        print ("Must be to two decimal places, separated by commas, for each of your respective clients: Paul, John, James, Declan, Mike, Ian. ")
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

"""  
FUNCTION 4: Calculating change in weight
"""
def calculate_weight_change(week_ends_row):
    """  
    Compare week_ends weighin data with week_starts weighin data and calculate the change for each client.
    The change in weight will be calculated and added to the insights tab as the week 9 row.   
    the change in weight is defined as the week_starts weighin figure subtracted from the week_ends weighin figure:
    - Positive change in weight indicates weight gain
    - Negative change in weight indicates weight loss
    Need to review how to get new_weight_change_data to two decimal points
    """

    print("Calculating week 9 change in weight for Paul, John, James, Declan, Mike and Ian...")
    week_starts = SHEET.worksheet("week_starts").get_all_values()
    week_starts_row = (week_starts[-1])
    
    weight_change_data = []
    for week_starts, week_ends in zip(week_starts_row, week_ends_row):
        weight_change = week_ends - float(week_starts)
        weight_change_data.append(weight_change)
    
    return weight_change_data 

"""  
FUNCTION 5:INSERTING WEIGHT_CHANGE_DATA INTO GOOGLE SHEETS
"""
def update_weightchange_worksheet(weight_change_data):
    """ 
    Update weight change worksheet, add new row with the weight change values previously calculated.
    """
    print ("Updating weight change info for week 9...\n")
    weightchange_worksheet = SHEET.worksheet("weight_change")
    weightchange_worksheet.append_row(weight_change_data)
    print ("Week 9 weight change info updated successfully.\n")

"""  
FUNCTION 6: Calculating variance-Expected weight loss versus actual weight 
loss loop
"""

""" 
FUNCTION 8: Moving variance info into google sheets
"""

"""  
FUNCTION 9: Divide clients into two lists: Those that met expectation and those
that didn't, with if else. Those that did=green, those that did not=red
"""  
"""  
FUNCTION 10:
For the clients tht did not meet expectation-load their feedback comments to
the python terminal for the personal trainer to see. 
"""

"""FUNCTION 11:
Gives personal trainer (user) the option to retrieve contact details for clients
who did not meet expectation so he can contact them (e.g. if feedback not adeuqate)


MAIN FUNCTION-BOTTOM OF FILE-CONTAINS ALL FUNCTION CALLS
"""
def main():
    """ 
    Run all of the functions contained in the program-contains calls for 
    all functions...login function to be inserted
    """
    data = get_weighin_data()
    weighin_data = [float(num) for num in data]
    update_weighin_worksheet(weighin_data)
    new_weight_change_data = calculate_weight_change(weighin_data)
    update_weightchange_worksheet(new_weight_change_data)



print("Welcome to 'My Weigh or the High Weigh', the app built to assist personal trainers to track their clients!")
main()



