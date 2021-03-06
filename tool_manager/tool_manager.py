# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# manufacturer: string
# purchase_date: number (year)
# durability: number (year)


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
    table = data_manager.get_table_from_file('tool_manager/tools.csv')
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
        available_tools = get_available_tools(table)
        ui.print_result(available_tools, 'Produckt before their durability time')
    elif option == "6":
        average_durability = get_average_durability_by_manufacturers(table)
        ui.print_result(average_durability, 'Manufacture ; average durability')
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
               "Which items has not yet exceeded their durability?",
               "What are the average durability time for each manufacturer?"]

    ui.print_menu("----> Tool manager", options, "Go back to the main menu")


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
    title_list = ['id', 'name', 'manufacturer', 'purchase_date', 'durability']
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
    list_labels = ['Enter name: ',
                   'Enter manufacturer: ',
                   'Enter purchase date (year): ',
                   'Enter durability (year(s)): ']

    inputs = [common.generate_random(table)]
    inputs += ui.get_inputs(list_labels, '')
    table.append(inputs)
    data_manager.write_table_to_file('tool_manager/tools.csv', table)

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
            i += 2
        else:
            i += 1
    if i == len(table):
        ui.print_string('There is no such ID.')

    data_manager.write_table_to_file('tool_manager/tools.csv', table)

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

    list_labels = ['Enter name: ',
                   'Enter manufacturer: ',
                   'Enter purchase date (year): ',
                   'Enter durability (year(s)): ']

    inputs = [id_to_keep]
    inputs += ui.get_inputs(list_labels, '')
    table.append(inputs)
    data_manager.write_table_to_file('tool_manager/tools.csv', table)

    return table


# special functions:
# ------------------

# the question: Which items has not yet exceeded their durability ?
# return type: list of lists (the inner list contains the whole row with their actual data types)
#
# @table: list of lists
def get_available_tools(table):
    '''Returns list with subscribed customer names and emails
    Parameters
    ----------
    table : list

    Returns
    -------
    exceeded_durability : list of lists

    '''
    proper_table = common.str_to_int_in(table)
    not_exceeded_durability = []
    current_year = 2017

    for information in proper_table:
        if (current_year - int(information[-2])) <= int(information[-1]):
            not_exceeded_durability.append(information)

    return not_exceeded_durability


# the question: What are the average durability time for each manufacturer?
# return type: a dictionary with this structure: { [manufacturer] : [avg] }
#
# @table: list of lists
def get_average_durability_by_manufacturers(table):

    '''Returns list with subscribed customer names and emails
    Parameters
    ----------
    table : list

    Returns
    -------
    manufacturer_avr : dictionary { [manufacturer] : [average] }
    '''

    manufacturer_avr = {}

    for information in table:
        if information[-3] in manufacturer_avr:
            manufacturer = information[-3]
            durability = int(information[-1])
            manufacturer_avr[manufacturer] += [durability]
        else:
            manufacturer = information[-3]
            durability = int(information[-1])
            manufacturer_avr[manufacturer] = [durability]

    for manufacturer in manufacturer_avr:
        sum_of_durability = 0

        for number in manufacturer_avr[manufacturer]:
            sum_of_durability += number

        average = sum_of_durability / len(manufacturer_avr[manufacturer])

        manufacturer_avr[manufacturer] = average

    return manufacturer_avr
