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

def login():
    """
    User must enter username and password before allowing user to log in and access confidential 
    information.
    """
    
    acceptable_username = False

    login = SHEET.worksheet('login_info')

    username_data = login.col_values(1)
    password_data = login.col_values(2)

    while acceptable_username is False:
        username = input('Username:\n')

        try: username in username_data:
            acceptable_username = True
        except ValueError():
            print(f"Username: '{username}', is incorrect.\
                \nRe-enter\n")

    username_place = username_data.index(username)

    acceptable_password = False
    while acceptable_password is False:
        password = input('Password:\n')

        try: password == password_data[username_place]:
            print(f"Welcome back {username}")
            acceptable_password = True
        except PermissionError():
            print(f"Password: {password}, is incorrect, please try again")

    return username

username = input("Username: ")

while True:
    try:
        x = input('Enter a number.')
        print(f'Number is {x}')
    except ValueError:
        print('Wrong username')

password = input("Password: ")
while True:
    try:
        x = input('Enter a number.')
        print(f'Number is {x}')
    except PermissionError:
        print('Wrong password')
"""
Error handling...Insert Try: Except: for username and password being correct
"""
print("Hello " + username + ", welcome to your Personal Training client tracker app,
 'My Weigh or the High Weigh.' "

def print_last_weighin():
    """
    User can opt to print out the last list of weights in kg per the last weigh-in
    for each of the six clients. (Weights in kg at start of week)
    """
    print()

def enter_current_weighins():
    input("Please enter week {} weigh-in information for the your respective clients,  Paul, John, James, Declan, Mike, Ian")
    """ 
    User is prompted to enter the end-of-week weights for the latest week (week 9) for each of
    the six clients.
    Error handling is considered here, as it is important six values are input in 
    numeric, float format as they should be in kg for each client.
    The weigh-in information must be in a certain order (order of names), must be in numerical format,
    must be to two decimal places, must be an entry for each of the six clients, can
    be 0.00.
    Once the six weigh-in values are entered, they should update the google sheets page accordingly
    Must be a float, must be numeric, must be six values
    look into format try:, except:, else:, else:, finally:
    """

    while True:
    try:
        x = float(input('Enter the last weigh-in results for your clients.'))
        print(f'The respective week week-end weigh-ins for Paul, John, James, Declan, 
         Mike and Ian are {x}')
    except ValueError:
        print('Must be in kg, to two decimal places')

    while True:
    try:
        x = int(input('Enter the last weigh-in results for your clients.'))
        print(f'Number is {x}')
    except ValueError:
        print('Must enter weigh-in info for all six clients')

def worth_the_weight_loss (): 
    """ 
    This function calculates and prints a list of the week 9 change in weight (in kg and %) for each of the six clients  
    Format: Name: kg/% in order Paul, John, James, Declan, Mike and Ian
    """

def weight_variance ():
    """  
    This function activates a calculation in google sheets that compares the actual 
    weight lost in week 9 (from the worth_the_weight function) to the expected weight 
    loss (which is the average weight loss per client for first 8 weeks)
    Two separate lists are printed, the first list is printed in green for the clients
    that met or exceeded weight loss expectation (if else formuale <=).
    The second list is in red for the clients that have not met their weight loss expectation
    Is it possible to change font colour
    Green font= met/exceeded weight loss expectation
    Red font= did not meet weight loss expectation
    """
def contact_red_clients ():
    """
    This function enables the user to print a list of the names of the clients that
    did not meet their weight loss expectation this week. It draws from google sheets
    also to print the email information of the client so that the user (personal trainer)
    can contact the client to get feedback about why expectations were not met.
    All feedback will be logged to Google Sheets 
    """
    print()
def average_loss ():
    """ 
    Calculate average weight lost in total over entire 9 week term for clients
    Calculate average weight lost per week for clients
    """

 def max_loss ():
    """  
    Calculate maximum total weight lost over 9 weeks-list client and weight loss in kg
    Calculate maximum weight lost in week 9-list client and weight lost in kg
     f "The highest overall weight loss was {}kg by {}"
     f "The highest weight loss this week was {}kg by {}"
    """

 def min_loss ():
  """ 
  Calculate minimum total weight lost over 9 weeks-list client and weight loss in kg
  Calculate minimum weight lost in week 9-list client and weight lost in kg
   f "The lowest overall weight loss was {}kg by {}"
   f "The lowest weight loss this week was {}kg by {}"
  """

 def weight_loss_range ():
  """  
  F string printed to python terminal
  Lowest total weight loss in kg-Highest total weight loss in kg over 9 weeks listed
  Lowest total weight loss in kg-highest total weight loss in kg for week 9 only listed
    f "The overall weight loss ranged from {}kg to {}kg"
    f "The week 9 weight loss ranged from {}kg to {}kg"
  """         


def main():
    """
    Run all program functions-important to have at end of python code...can be commented out in order to test 
    individual functions
    """
    data = get_data()
    weighin_data = [float(num) for num in data]
    update_worksheet(week_ends, "week-end data")
    new_weightloss_data = calculate_weightloss_data(insights)
    update_worksheet(new_weightloss_data, "insights")
    update_worksheet(variancw, "variance")



print("Welcome to 'My Weigh or the High Weigh' Data Automation")
main()