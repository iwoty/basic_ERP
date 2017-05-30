# data structure:
# kH14Ju#&;1;21;2016;in;31
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# month: number
# day: number
# year: number
# type: string (in = income, out = outcome)
# amount: number (dollar)


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
    while True:
        handle_menu()
        try:
            if choose() == 'back_to_main':
                break
        except KeyError as err:
            ui.print_error_message(err)


def choose():
    table = data_manager.get_table_from_file('accounting/items.csv')
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    if option == "1":
        show_table(table)
    elif option == "2":
        add(table)
    elif option == "3":
        remove(table, id_)
    elif option == "4":
        update(table, id_)
    elif option == "5":
        which_year_max(table)
    elif option == "6":
        avg_amount(table, year)
    elif option == "0":
        return 'back_to_main'
    else:
        raise KeyError("There is no such option.")


def handle_menu():
    options = ["Show table",
               "Add to table",
               "Remove from table",
               "Update table",
               "Which year has the highest profit?",
               "What is the average (per item) profit in a given year?"]

    ui.print_menu("----> Accounting manager", options, "Go back to the main menu")


# print the default table of records from the file
#
# @table: list of lists
def show_table(table):
    print(table)

# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):

    # your code

    return table


# Remove the record having the id @id_ from the @list, than return @table
#
# @table: list of lists
# @id_: string
def remove(table, id_):

    # your code

    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
#
# @table: list of lists
# @id_: string
def update(table, id_):

    # your code

    return table


# special functions:
# ------------------

# the question: Which year has the highest profit? (profit=in-out)
# return the answer (number)
def which_year_max(table):

    # your code

    pass


# the question: What is the average (per item) profit in a given year? [(profit)/(items count) ]
# return the answer (number)
def avg_amount(table, year):

    # your code

    pass
