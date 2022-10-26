import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')


def get_sales_data():
    """
    Get sales figures input from the user.
    Adjust to get week 9 week-end weigh-ins from user...week 9 week start
    data already provided...
    """
    while True:
        print("Please enter week-end weigh-in data from week 9.")
        print("Should enter weight for each of the six clients in kg to two decimal places.")
        print("Example: 70.45,82.40,78.50,79.20,85.20,90.50\n")

        data_str = input("Enter week 9 end of week weigh-in data here:\n")

        sales_data = data_str.split(",")

        if validate_data(sales_data):
            print("You entered the week 9 weights!")
            break

    return sales_data

def validate_data(values):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly 6 values.
    Weight in kg to two decimal places, should not be in word format
    and should not have more or less than two decimal places
    """
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 weigh-in values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True

    """
    Weight in kg to two decimal places, should not have more or less than two
    decimal places
    """

try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"Kg must be to two decimal places, you entered {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


def update_worksheet(data, worksheet):
    """
    Receives a list of integers to be inserted into a worksheet
    Update the relevant worksheet with the data provided

    This needs to be adjusted to flow into the week-end of week9 weigh in information
    """
    print(f"Updated {worksheet} worksheet.../n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data) 
    print(f"{worksheet} worksheet updated successfully\n")

def calculate_surplus_data(sales_row):
    """
    Compare sales with stock and calculate the surplus for each item type.
    The surplus is defined as the sales figure subtracted from the stock:
    - Positive surplus indicates waste
    - Negative surplus indicates extra made when stock was sold out.

    This function will be used to calculate the change in weight for the latest row
    """
    print("Calculating week 9 weight change...\n")
    stock = SHEET.worksheet("stock").get_all_values()
    stock_row = stock[-1]

    surplus_data = []
    for stock, sales in zip (stock_row, sales_row):
        surplus = int(stock) - sales 
        surplus_data.append(surplus)
    return surplus_data 

def get_last_5_entries_sales():
    """
     Collects columns of data from sales worksheet, collecting
    the last 5 entries for each sandwich and returns the data
    as a list of lists.

    Get week nine weight change information and produce this as a list
    """
    sales = SHEET.worksheet("sales")

    columns = []
    for ind in range(1,7):
        column = sales.col_values(ind)
        columns.append(column[-5:])
    
    return columns 

def calculate_stock_data(data):
    """
    Calculate the average stock for each item type, adding 10%

    Update tihs function to calcuate the average weight loss on a week to week basis
    """
    print("Calculating average weight loss...\n")
    new_stock_data = []

    for column in data:
        int_column = [int(num) for num in column]
        average = sum(int_column)/len(int_column)
        stock_num = average * 1.1
        new_stock_data.append(round(stock_num))
    
    return new_stock_data

def main():
    """
    Run all program functions
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