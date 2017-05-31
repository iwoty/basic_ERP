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
        year = input("year:")
        avg_amount(table, year)
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
               "Which year has the highest profit?",
               "What is the average (per item) profit in a given year?"]

    ui.print_menu("----> Accounting manager", options, "Go back to the main menu")


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
    title_list = ['id', 'month', 'day', 'year', 'type', 'amount']
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
    list_labels = ['Enter month: ', 'Enter day: ', 'Enter year: ', 'Enter type (in/out): ', 'Enter amount: ']
    inputs = [common.generate_random(table)]
    inputs += ui.get_inputs(list_labels, '')
    table.append(inputs)
    data_manager.write_table_to_file('accounting/items.csv', table)
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
def sum_profits(year, table):
    sum_profit_in = 0
    sum_in = []
    for line in table:
        line[5] = int(line[5])
        if line[3] == year and line[4] == 'in':

            sum_in.append(line[5])

            for i in sum_in:
                sum_profit_in += i


    sum_profit_out = 0
    sum_out = []
    for line in table:
        line[5] = int(line[5])
        if line[3] == year and line[4] == 'out':
            sum_out.append(line[5])

            for i in sum_out:
                sum_profit_out += i

    profit = sum_profit_in - sum_profit_out

    return profit, year


# the question: Which year has the highest profit? (profit=in-out)
# return the answer (number)
def which_year_max(table):
    '''???

    Args:
        param1: ???
        param2: ???

    Returns:
        ?????

    '''
    years = []
    for line in table:
        if not line[3] in years:
            years.append(line[3])

    profits = []

    for i in range(len(years)):
        profits.append(sum_profits(years[i], table))

    max_profit = max([tupl[0] for tupl in profits])

    for tupl in profits:
        if tupl[0] == max_profit:
            max_profit_year = tupl[1]

    print(max_profit_year)
    return max_profit_year


# the question: What is the average (per item) profit in a given year? [(profit)/(items count) ]
# return the answer (number)
def avg_amount(table, year):
    '''???
    Args:
        param1: ???
        param2: ???

    Returns:
        ?????

    '''
    profit, year = sum_profits(year, table)
    print(profit)
    amount = 0

    for line in table:
        if line[3] == year:
            amount += 1
    average = profit / amount
    print(average)
    return average
