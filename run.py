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
FUNCTION 5:Inserting weight change data into google sheets
"""
def update_weightchange_worksheet(weight_change_data):
    """ 
    Update weight change worksheet, add new row including the weight change values previously calculated in function 4.
    """
    print ("Updating weight change info for week 9...\n")
    weightchange_worksheet = SHEET.worksheet("weight_change")
    weightchange_worksheet.append_row(weight_change_data)
    print ("Week 9 weight change info updated successfully.\n")

"""  
FUNCTION 6: Calculating variance-Expected weight loss versus actual weight 
loss loop-format of function based on function 4
"""
def calculate_variance(weight_change_row):
    """  
    Compare weight_change_data with expected_change_data and calculate the variance for each client.
    The variance from expectation will be calculated and added to the variance tab as the week 9 row.   
    The variance is defined as the expected_change_data figure subtracted from the weight_change_data figure:
    - Positive variance indicates that weight loss expectation has not been met
    - Negative variance in weight indicates that weight loss expectation has been met
    Positive values print list of associated names in red to signify failure or that further action is required
    Negative values print list of associated names in green, signifying no further action needed
    *Note-function must be run after weight_change function so that the weight_change_data is populated and available for the necessary calculation
    """

    print("Calculating week 9 variance from expected weight loss for Paul, John, James, Declan, Mike and Ian...")
    expected_wc = SHEET.worksheet("expected_wc").get_all_values()
    expected_wc_row = (expected_wc[-1])
    
    variance_data = []
    for expected_wc, weight_change in zip(expected_wc_row, weight_change_row):
        variance = weight_change - float(expected_wc)
        variance_data.append(variance)
    
    return variance_data 

""" 
FUNCTION 7 : Inserting variance data into google sheets
"""
def update_variance_worksheet(variance_data):
    """ 
    Update variance worksheet, add new row including the variance values previously calculated in function 6.
    """
    print ("Updating variance info for week 9...\n")
    variance_worksheet = SHEET.worksheet("variance")
    variance_worksheet.append_row(variance_data)
    print ("Week 9 variance info updated successfully.\n")

"""  
FUNCTION 8: Variance lists

"""  
def variance_split():
    """ 
    Divide clients into two lists: Those that met expectation (negative variance) and those
    that did not meet expectation (potentially use an if else formula).
    The list of people that did meet expectation should be in green.
    The list of people that did not meet expectation should be in red. 
    """

"""  
FUNCTION 9: Red list feedback
"""
def redlist_feedback():
"""
For the red list, clients that did not meet expectation give the
user the option to load their feedback comments to the python terminal
"""

"""FUNCTION 10: Contact red list
"""
def contact_redlist():
"""
Gives personal trainer (user) the option to retrieve contact details for clients
who did not meet expectation so he can contact them (e.g. if feedback not adequate)
"""

"""  
FUNCTION 11: Range function.
"""
def weight_change_total_range():
"""
Calculates client with highest total weight loss (max)
Calculates client with lowest total weight loss (min)
Prints an f string to the python terminal f"The total weight loss over the
course of the programme so far has ranged from {}kg to {}kg."
"""

"""FUNCTION 12:Average weight loss function.
"""
def weight_change_total_average():
"""
Calculates the average total weight loss per client over the course of the programme and prints
f string (f"The average total weight loss for the programme to date has been {}kg)
"""


"""
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
    new_variance_data = calculate_variance(new_weight_change_data)
    update_variance_worksheet(new_variance_data)



print("Welcome to 'My Weigh or the High Weigh', the app built to assist personal trainers to track their clients!")
main()



