# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# email: string
# subscribed: boolean (Is she/he subscribed to the newsletter? 1/0 = yes/not)


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
    table = data_manager.get_table_from_file('crm/customers.csv')
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
        longest_name_id = get_longest_name_id(table)
        ui.print_result(longest_name_id, 'ID of customer with longest name')
    elif option == "6":
        subscribers_emails = get_subscribed_emails(table)
        ui.print_result(subscribers_emails, 'Customer email ; Subscribed customer name')
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
               "What is the id of the customer with the longest name?",
               "Which customers has subscribed to the newsletter?"]

    ui.print_menu("----> Customer Relationship Management (CRM)", options, "Go back to the main menu")


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
    title_list = ['id', 'name', 'email', 'subscribed']
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
    list_labels = ['Enter name: ', 'Enter email: ', 'Is subscribed? ']
    inputs = [common.generate_random(table)]
    inputs += ui.get_inputs(list_labels, '')
    table.append(inputs)
    data_manager.write_table_to_file('crm/customers.csv', table)
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
    data_manager.write_table_to_file('crm/customers.csv', table)
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

    list_labels = ['Enter name: ', 'Enter email: ', 'Is subscribed? ']
    inputs = [id_to_keep]
    inputs += ui.get_inputs(list_labels, '')
    table.append(inputs)
    data_manager.write_table_to_file('crm/customers.csv', table)
    return table


# special functions:
# ------------------


# the question: What is the id of the customer with the longest name ?
# return type: string (id) - if there are more than one longest name, return the first of ascending alphabetical order
def get_longest_name_id(table):
    '''Returns id of longest customer name
    Parameters
    ----------
    table : list

    Returns
    -------
    customer_id : string
    '''

    dic_customer_id = {}
    list_of_longest_names = []

    for information in table:
        dic_customer_id[information[1]] = information[0]

    longest_name = max(len(key) for key in dic_customer_id.keys())

    for key in dic_customer_id.keys():
        if len(key) == longest_name:
            list_of_longest_names.append(key)

    alphabetical_longest_name = min(list_of_longest_names)

    customer_id = (dic_customer_id[alphabetical_longest_name])

    return customer_id


# the question: Which customers has subscribed to the newsletter?
# return type: list of string (where string is like email+separator+name, separator=";")
def get_subscribed_emails(table):
    '''Returns list with subscribed customer names and emails
    Parameters
    ----------
    table : list

    Returns
    -------
    list_of_subscriber : list of strings
    '''

    list_of_subscriber = []

    for subscriber in table:
        if subscriber[3] == '1':
            information = subscriber[2] + ';' + subscriber[1]
            list_of_subscriber.append(information)

    return list_of_subscriber
