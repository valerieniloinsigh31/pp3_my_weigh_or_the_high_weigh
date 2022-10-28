import gspread
from google.oauth2.service_account import Credentials
import math

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
    Gets username and password before allowing user to log in and access confidential 
    information.
    """

def print_last_weighin():
    """
    User can opt to print out the last list of weights in kg per the last weigh-in
    for each of the six clients
    """

def enter_currentweighins():
    """ 
    User is prompted to enter the weekend weights for the end of week 9 for each of
    the six clients.
    error handling: try: except:
    Must be in a certain order (order of names), must be in numerical format,
    must be to two decimal places, must be an entry for each of the six clients, can
    be 0.00.
    Once this is entered it should update the google sheets page accordingly
    """

def worth_the_weight (): 
    """ 
    This function prints a list of the six clients with the week 9 change in weight 
    kg and % per client printed to the python terminal
    """

def weight_variance ():
    """  
    This function activates a calculation in google sheets that compares the actual 
    weight lost in week 9 (from the worth_the_weight function) to the expected weight 
    loss (which is the average weight loss per client for first 8 weeks)
    Two separate lists are printed, the first list is printed in green for the clients
    that met or exceeded weight loss expectation (if else formuale <=).
    The second list is in red for the clients that have not met their
    weight loss expectation
    """
def contact_red_clients ():
    """
    This function enables the user to print a list of the names of the clients that
    did not meet their weight loss expectation this week. It draws from google sheets
    also to print the email and number of the client so that the user (personal trainer)
    can contact the client to get feedback about why expectations were not met.
    All feedback will be logged to Google Sheets 
    """
def average_loss ():
    """ 
    """

 def max_loss ():
    """  
    """

 def min_loss ():
  """ 
  """

 def weight_loss_range ():
  """  
  """         


def main():
    """
    Run all program functions-important to have at end of python code...can be commented out in order to test 
    individual functions
    """
    data = get_sales_data()
    sales_data = [int(num) for num in data]
    update_worksheet(sales_data, "sales")
    new_surplus_data = calculate_surplus_data(sales_data)
    update_worksheet(new_surplus_data, "surplus")
    sales_columns = get_last_5_entries_sales()
    stock_data = calculate_stock_data(sales_columns)
    update_worksheet(stock_data, "stock")



print("Welcome to 'My Weigh or the High Weigh' Data Automation")
main()