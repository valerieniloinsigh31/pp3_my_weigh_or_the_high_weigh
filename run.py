import gspread
from google.oauth2.service_account import Credentials
import math
from datetime import datetime
import os
from pprint import pprint 
import sys
sys.path.append("/usr/local/lib/python3.8/dist-packages/")
import colorama
from colorama import Fore 
colorama.init(autoreset=True)


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
COVER IMAGE FOR APP: From Ascii Art Archive
"""
def print_bodybuilder():
    """
    Prints the graphic of a bodybuilder, as
    extracted from https://www.asciiart.eu/sports-and-outdoors/other. Art by Joan Stark
    """
    print(''' 
    
                 ,#####,
                 #_   _#
                 |a` `a|
                 |  u  |
                 \  =  /
                 |\___/|
        ___ ____/:     :\____ ___
      .'   `.-===-\   /-===-.`   '.
     /      .-"""""-.-"""""-.      \\
    /'             =:=             '\\
  .'  ' .:    o   -=:=-   o    :. '  `.
  (.'   /'. '-.....-'-.....-' .'\   '.)
  /' ._/   ".     --:--     ."   \_. '\\
 |  .'|      ".  ---:---  ."      |'.  |
 |  : |       |  ---:---  |       | :  |
  \ : |       |_____._____|       | : /
  /   (       |----|------|       )   \\
 /... .|      |    |      |      |. ...\\
|::::/'' jgs /     |       \     ''\::::|
'""""       /'    .L_      `\       """"'
           /'-.,__/` `\__..-'\\
          ;      /     \      ;
          :     /       \     |
          |    /         \.   |
          |`../           |  ,/
          ( _ )           |  _)
          |   |           |   |
          |___|           \___|
          :===|            |==|
           \  /            |__|
           /\/\           /"""`8.__
           |oo|           \__.//___)
           |==|
           \__/
    ''')

""" 
FUNCTION 1: Log in to access database, using login and password from google sheets
"""
def user_login():
    """
    Get username and password from the user, validate from data saved on google sheets
    could use try: except and permissionerror
    """
    login= SHEET.worksheet("login_info").get_all_values()
    username_valid= (login[1])
    password_valid= (login[2])

    username_input = input('Enter your username here:\n')
    
    if username_input != ''.join(username_valid):
        print("Invalid username, try again.")
        return user_login()
    print('Hi personal_trainer, please enter your usual password."')

    password_input = input('Enter your password here:\n')

    if password_input != ''.join(password_valid):
        print("Invalid password, try again\n")
        return user_login()
    print('Welcome back personal_trainer.\n')
"""
FUNCTION 2: Collect latest weigh-in data from user and includes error handling validation
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
FUNCTION 3: Move weigh-in data to the google sheets.
"""
def update_weighin_worksheet(data):
    """ 
    Update week-ends weigh-in worksheet, add new row with the values input by the user. These values should
    also be added to the week_starts tab at the end of the run of an app so that the app rolls on each run
    """
    print ("Updating end-of-week weigh-in info for week 9...\n")
    weighin_worksheet = SHEET.worksheet("week_ends")
    weighin_worksheet.append_row(data)
    print ("Week 9 end-of-week weigh-in info updated successfully.\n")

"""  
FUNCTION 4: Calculate change in weight for latest week
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
FUNCTION 5: Move weight change data into google sheets
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
FUNCTION 6: Calculate variance. Variance being the difference 
between expected weight loss and actual weight 
loss. The format of this function is based on function 4.
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
FUNCTION 7: Move variance data into google sheets
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
FUNCTION 8: Divide variance into two lists: Clients who met expectation and clients that didn't

"""  
def variance_split():
    """ 
    Divide clients into two lists: Those that met expectation (negative variance) and those
    that did not meet expectation.
    The list of people that did meet expectation should be in green.
    The list of people that did not meet expectation should be in red. 
    Print only names, not values, use index or split (row 1 only)
    """

    print("Dividing out client results into those that met their weight loss targets and those who did not...")
    green_list = SHEET.worksheet("variance_green").get_all_values()
    green_list_row = (green_list[0])
    print(Fore.GREEN + 'Firstly, here is a list of clients who met their expectation.')
    print(green_list_row)

    red_list = SHEET.worksheet("variance_red").get_all_values()
    red_list_row = (red_list[0])
    print(Fore.RED + 'Now, here is a list of clients who did not meet their expectation.')
    print(red_list_row)


"""  
FUNCTION 9: Gives user option to print client feedback from that week
"""
def list_feedback():
    """
    Gives the user the option to print the week 9 stored client 
    feedback comments to the python terminal.
    Lists clients who did not meet expectation that week as more inclined to want
    to access their feedback.
    """
    print("Well so there you have it, the culprits who did not stay on track are as follows:")
    red_list = SHEET.worksheet("variance_red").get_all_values()
    red_list_row = (red_list[0])
    print(red_list_row)
    print("Have a look at some of the feedback provided by clients during the week.")
    
    """   
    Nested functions: One per client, Paul, John, James, Declan, Mike, Ian
    """
    def paul():
        paul_feedback = SHEET.worksheet("logged_feedback").get_all_values()
        paul_feedback_row = (paul_feedback[0])
        print(paul_feedback_row)
        return list_feedback()

    def john():
        john_feedback = SHEET.worksheet("logged_feedback").get_all_values()
        john_feedback_row = (john_feedback[3])
        print(john_feedback_row)
        return list_feedback()

    def james():
        james_feedback = SHEET.worksheet("logged_feedback").get_all_values()
        james_feedback_row = (james_feedback[6])
        print(james_feedback_row)
        return list_feedback()

    def declan():
        declan_feedback = SHEET.worksheet("logged_feedback").get_all_values()
        declan_feedback_row = (declan_feedback[9])
        print(declan_feedback_row)
        return list_feedback()

    def mike():
        mike_feedback = SHEET.worksheet("logged_feedback").get_all_values()
        mike_feedback_row = (mike_feedback[12])
        print(mike_feedback_row)
        return list_feedback()

    def ian():
        ian_feedback = SHEET.worksheet("logged_feedback").get_all_values()
        ian_feedback_row = (ian_feedback[15])
        print(ian_feedback_row)
        return list_feedback()
        
    print(Fore.BLUE+"Please enter the number of a client you would like to get a feedback comment from-maybe someone who did not meet expectation? Select exit to move on.\n")
    print(Fore.BLUE+'1. Paul')
    print(Fore.BLUE+'2. John')
    print(Fore.BLUE+'3. James')
    print(Fore.BLUE+'4. Declan')
    print(Fore.BLUE+'5. Mike')
    print(Fore.BLUE+'6. Ian')
    print(Fore.BLUE+'7. Exit')
    print(Fore.BLUE+'\nPlease select an option by entering a number between 1 and 7')

    choice = input(Fore.BLUE+'Enter your single digit choice here:\n')

    if choice == '1':
         paul()
    elif choice == '2':
        john()
    elif choice == '3':
        james()
    elif choice == '4':
        declan()
    elif choice == '5':
        mike()
    elif choice == '6':
        ian()
    elif choice == '7':
        print(Fore.RED+'Okay-you are done with the comments !')
    else:
        print(Fore.BLUE+'Invalid selection. Please enter a digit between 1 and 7\n')
       
    contact = input(Fore.YELLOW+'Would you like to see the contact information? Please type y to access contacts or n to exit.\n')
   
    if contact == 'y':
        print(Fore.YELLOW+"Here is the contact info.")
        contact_client()
    else: 
        exit_app()

"""
FUNCTION 10: Contact client list
"""
def contact_client():
    """
    Gives personal trainer (user) the option to retrieve contact details for clients
    so he can contact them. This may be most relevant for clients who did not
    meet expectation when the feedback that they have offered is not adequate.
    Format of function is similar to function 9.
    """
    
    """   
    Nested functions: One per client, Paul, John, James, Declan, Mike, Ian
    """
    def paul_contact():
        paul_contact = SHEET.worksheet("contact").get_all_values()
        paul_contact_row = (paul_contact[1])
        print(paul_contact_row)
        return contact_client()

    def john_contact():
        john_contact = SHEET.worksheet("contact").get_all_values()
        john_contact_row = (john_contact[2])
        print(john_contact_row)
        return contact_client()

    def james_contact():
        james_contact = SHEET.worksheet("contact").get_all_values()
        james_contact_row = (james_contact[3])
        print(james_contact_row)
        return contact_client()

    def declan_contact():
        declan_contact = SHEET.worksheet("contact").get_all_values()
        declan_contact_row = (declan_contact[4])
        print(declan_contact_row)
        return contact_client

    def mike_contact():
        mike_contact = SHEET.worksheet("contact").get_all_values()
        mike_contact_row = (mike_contact[5])
        print(mike_contact_row)
        return contact_client()

    def ian_contact():
        ian_contact = SHEET.worksheet("contact").get_all_values()
        ian_contact_row = (ian_contact[6])
        print(ian_contact_row)
        return contact_client()
        
    print(Fore.YELLOW+"Please enter the number for the client you would like to get contact details for?\n")
    print(Fore.YELLOW+'1. Paul')
    print(Fore.YELLOW+'2. John')
    print(Fore.YELLOW+'3. James')
    print(Fore.YELLOW+'4. Declan')
    print(Fore.YELLOW+'5. Mike')
    print(Fore.YELLOW+'6. Ian')
    print(Fore.YELLOW+'7. Exit')
    print(Fore.YELLOW+'\nPlease select an option by entering a number between 1 and 7')

    choice = input(Fore.YELLOW+'Enter your single digit choice here:\n')

    if choice == '1':
         paul_contact()
    elif choice == '2':
        john_contact()
    elif choice == '3':
        james_contact()
    elif choice == '4':
        declan_contact()
    elif choice == '5':
        mike_contact()
    elif choice == '6':
        ian_contact()
    elif choice == '7':
        print(Fore.RED+'No need to make further contact now.')
        exit_app()
    else:
        print(Fore.RED+'Invalid selection. Please enter a digit between 1 and 7\n')
        

"""  
FUNCTION 11: Range function.
"""
def weight_change_total_range():
    """
    Pulls in value from max and min tabs in google sheet
    Prints an f string to the python terminal f"The total weight loss over the
    course of the programme so far has ranged from {}kg to {}kg."
    variable 1=lowest kg extracted from google sheets
    print(f"")
    """

"""FUNCTION 12:Average weight loss function.gi
"""
def weight_change_total_average():
    """
    Calculates the average total weight loss per client over the course of the programme and prints
    f string (f"The average total weight loss for the programme to date has been {}kg)
    """

    """  
    FUNCTION 13: Exit app (and reset week 9 to blank-to accommodate manual calcs
    """

def exit_app():
    """ 
    Must be selected by user to exit app and prompts pop function to remove the appended rows so that
    app functionality resets. This is because the variance split tabs are not automated so
    entire app must be rest so next user can use app 
    Lines that need to have rows removed...week_ends, weight_change, variance)
    """
    """  
    Nested function-updates week_starts data to include this weeks week-end data so app will work on next run.
    """
    #start_data=SHEET.worksheet("week_ends").row_values(-1)
    #def update_week_starts_for_latest (start_data):
        #weekstart_worksheet = SHEET.worksheet("week_starts")
        #weekstart_worksheet.append_row(start_data)

    exit= input(Fore.BLUE+"Would you like to exit the app? Please type 'y' to exit, 'c' to return to contacts or 'f' to return to feedback.")
    if exit == 'y':
        print(Fore.BLUE+"Goodbye personal trainer, have a great week training!")
    elif exit == 'c':
        contact_client()
    elif exit == 'f':
        list_feedback()
    else:
        print(Fore.BLUE+"Invalid selection, please type 'y', 'c' or 'f'")
        
"""
MAIN FUNCTION-Calls all functions
"""

def main():
    """ 
    Run all of the functions contained in the program-contains calls for 
    all functions...login function to be inserted
    """
    print_bodybuilder()
    user_login()
    data = get_weighin_data()
    weighin_data = [float(num) for num in data]
    update_weighin_worksheet(weighin_data)
    new_weight_change_data = calculate_weight_change(weighin_data)
    update_weightchange_worksheet(new_weight_change_data)
    new_variance_data = calculate_variance(new_weight_change_data)
    update_variance_worksheet(new_variance_data)
    variance_split()
    list_feedback()
    contact_client()
    exit_app()
    


print(Fore.GREEN+"Welcome to 'My Weigh or the High Weigh', the app built to assist personal trainers to track their clients!")
main()



