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
 FUNCTION 2: Access and print weigh-in to date info
 """

last_weigh_in = SHEET.worksheet('last_weigh_in')

startdata = last_weigh_in.get_all_values()

print(startdata)

