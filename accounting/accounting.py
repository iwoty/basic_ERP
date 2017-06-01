# data structure:
# kH14Ju#&;1;21;2013;in;31
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
        remove(table, ui.get_inputs(['Enter ID of record to remove it: '], ''))
    elif option == "4":
        update(table, ui.get_inputs(['Enter ID of record to update it: '], ''))
    elif option == "5":
        max_year = which_year_max(table)
        ui.print_result(max_year, 'Year with the highest profit')
    elif option == "6":
        avg_amount(table, ui.get_inputs(['Enter a year to know the average profit: '], ''))
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
    '''Removing data

    Args:
        table (nested list): table with data
        id_ (string): id of item

    Returns:
        table (nested list): with item of inputed id removed - saved to the file

    '''
    i = 0
    id_ = ''.join(id_)  # change element of the list to string
    for row in table:
        if id_ == row[0]:
            table.pop(i)
        else:
            i += 1
    if i == (len(table)):
        ui.print_string('There is no such ID.')
    data_manager.write_table_to_file('accounting/items.csv', table)
    return table



# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
#
# @table: list of lists
# @id_: string

def update(table, id_):
    '''Updating an item by removing its values and adding new ones.

    Args:
        table (nested list): table with data
        id_ (string): id of item

    Returns:
        table (nested list): with item of inputed id removed - saved to the file

    '''
    id_to_keep = id_
    remove(table, id_)

    list_labels = ['Enter month: ', 'Enter day: ', 'Enter year: ', 'Enter type (in/out): ', 'Enter amount: ']
    inputs = [id_to_keep]
    inputs += ui.get_inputs(list_labels, '')
    table.append(inputs)
    data_manager.write_table_to_file('accounting/items.csv', table)
    return table



# special functions:
# ------------------
def sum_profits(year, table):
    '''Sums incomes, outcomes and calculates a profit

    Args:
        year: int
        table: list of lists

    Returns:
        profit: int
        year: int
    '''
    sum_profit_in = 0
    sum_profit_out = 0
    sum_in = []
    sum_out = []

    for line in table:

        line[5] = int(line[5])

        if int(line[3]) == int(year) and line[4] == 'in':
            sum_in.append(line[5])
            for i in sum_in:
                sum_profit_in += i

        if int(line[3]) == int(year) and line[4] == 'out':
            sum_out.append(line[5])
            for i in sum_out:
                sum_profit_out += i

    profit = sum_profit_in - sum_profit_out

    return profit, year


# the question: Which year has the highest profit? (profit=in-out)
# return the answer (number)
def which_year_max(table):
    '''Finds a year with the highest profit

    Args:
        table: list of lists

    Returns:
        max_profit_year: int

    '''
    years = []
    for line in table:
        if not int(line[3]) in years:
            years.append(int(line[3]))

    profits = []

    for i in range(len(years)):

        profits.append(sum_profits(years[i], table))

    max_profit = max([tupl[0] for tupl in profits])

    for tupl in profits:
        if tupl[0] == max_profit:
            max_profit_year = tupl[1]

    max_profit_year = int(max_profit_year)

    return max_profit_year


# the question: What is the average (per item) profit in a given year? [(profit)/(items count) ]
# return the answer (number)
def avg_amount(table, year):
    '''Counts the average profit for a given year
    Args:
        tabel : list of lists
        year : int

    Returns:
        avr_profit : int

    '''

    count = 0
    sum_in = 0
    sum_out = 0

    for information in table:
        if int(information[-3]) == year:
            count += 1
            if information[-2] == 'in':
                sum_in = sum_in + int(information[-1])
            elif information[-2] == 'out':
                sum_out = sum_out + int(information[-1])

    profit = sum_in - sum_out

    if count == 0:
        return None
    else:
        avr_profit = profit / count

    return avr_profit
