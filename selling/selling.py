# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# title: string
# price: number (the actual selling price in $)
# month: number
# day: number
# year: number
# month,year and day combined gives the date the purchase was made


# importing everything you need
import os
from importlib.machinery import SourceFileLoader
current_file_path = os.path.dirname(os.path.abspath(__file__))
# User interface module
ui = SourceFileLoader("ui", current_file_path + "/../ui.py").load_module()
# data manager module
data_manager = SourceFileLoader("data_manager", current_file_path + "/../data_manager.py").load_module()
# common module
common = SourceFileLoader("common", current_file_path + "/../common.py").load_module()


# start this module by a module menu like the main menu
# user need to go back to the main menu from here
# we need to reach the default and the special functions of this module from the module menu
#
def start_module():
    '''Starting this module.

    Args:
        None

    Returns:
        None

    '''
    while True:
        handle_menu()
        try:
            if choose() == 'back_to_main':
                break
        except KeyError as err:
            ui.print_error_message(err)


def choose():
    '''Menu choice of functions in module.

    Args:
        None

    Returns:
        None

    '''
    table = data_manager.get_table_from_file('selling/sellings.csv')
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    if option == "1":
        show_table(table)
    elif option == "2":
        add(table)
    elif option == "3":
        remove(table, ui.get_inputs(['Enter ID of record to remove it: '], ''))
    elif option == "4":
        update(table, id_)
    elif option == "5":
        lowest_price_product_id = get_lowest_price_item_id(table)
        ui.print_result(lowest_price_product_id, 'ID of lowest price product')
    elif option == "6":
        get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to)
        # najpierw input potem print
    elif option == "0":
        return 'back_to_main'
    else:
        raise KeyError("There is no such option.")


def handle_menu():
    '''Handling with options of menu.

    Args:
        None

    Returns:
        None

    '''
    options = ["Show table",
               "Add to table",
               "Remove from table",
               "Update table",
               "What is the id of the item that sold for the lowest price?",
               "Which items are sold between two given dates ? (from_date < birth_date < to_date)"]

    ui.print_menu("----> Selling manager", options, "Go back to the main menu")


# print the default table of records from the file
#
# @table: list of lists
def show_table(table):
    '''Shows(prints) table.

    Args:
        table (nested list): table with data

    Returns:
        None

    '''
    title_list = ['id', 'title', 'price', 'month', 'day', 'year']
    ui.print_table(table, title_list)


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):
    '''Adds data with randomly generater ID to table and saves it to file.

    Args:
        table (nested list): table with data

    Returns:
        table (nested list): with added item

    '''
    list_labels = ['Enter title: ', 'Enter price: ', 'Enter month: ', 'Enter day: ', 'Enter year: ']
    inputs = [common.generate_random(table)]
    inputs += ui.get_inputs(list_labels, '')
    table.append(inputs)
    data_manager.write_table_to_file('selling/sellings.csv', table)
    return table


# Remove the record having the id @id_ from the @list, than return @table
#
# @table: list of lists
# @id_: string
def remove(table, id_):
    '''???

    Args:
        param1: ???
        param2: ???

    Returns:
        ?????

    '''
    # your code

    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
#
# @table: list of lists
# @id_: string
def update(table, id_):
    '''???

    Args:
        param1: ???
        param2: ???

    Returns:
        ?????

    '''
    # your code

    return table


# special functions:
# ------------------

# the question: What is the id of the item that sold for the lowest price ?
# return type: string (id)
# if there are more than one with the lowest price, return the first of descending alphabetical order
def get_lowest_price_item_id(table):
    '''
    Parameters
    ----------
    table : list

    Returns
    -------
    information : string
    '''
    dic_price_id = {}
    products_price = []

    for price in table:
        products_price.append(price[2])

    lowest_price = min(products_price)

    for information in table:
        if information[2] == lowest_price:
            return information[0] # ID



# the question: Which items are sold between two given dates ? (from_date < birth_date < to_date)
# return type: list of lists (the filtered table)
def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):
    '''Finds items sold between two given dates

    Args:
        table: list of lists
        month_from: int
        day_from: int
        year_from: int
        month_to: int
        day_to: int
        year_to: int

    Returns:
        sold: list of lists

    '''
    sold = []

    for date in table:
        if year_from <= int(date[-1]) <= year_to:
            if month_from <= int(date[-3]) <= month_to:
                if day_from <= int(date[-2]) <= day_to:
                    sold.append([date[0], date[1], date[2]])
    return sold
