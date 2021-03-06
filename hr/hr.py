# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# birth_date: number (year)


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
    table = data_manager.get_table_from_file('hr/persons.csv')
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
        oldest_person = get_oldest_person(table)
        ui.print_result(oldest_person, 'Name of oldest customer')
    elif option == "6":
        close_to_average = get_persons_closest_to_average(table)
        ui.print_result(close_to_average, 'Name of customer with age closest to average age')
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
               "Who is the oldest person?",
               "Who is the closest to the average age?"]

    ui.print_menu("----> Human resources manager", options, "Go back to the main menu")


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
    title_list = ['id', 'name', 'birth_date']
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
                   'Enter birthdate (year): ']
    inputs = [common.generate_random(table)]
    inputs += ui.get_inputs(list_labels, '')
    table.append(inputs)
    data_manager.write_table_to_file('hr/persons.csv', table)
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
    data_manager.write_table_to_file('hr/persons.csv', table)
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
                   'Enter birthdate (year): ']
    inputs = [id_to_keep]
    inputs += ui.get_inputs(list_labels, '')
    table.append(inputs)
    data_manager.write_table_to_file('hr/persons.csv', table)
    return table


# special functions:
# ------------------

# the question: Who is the oldest person ?
# return type: list of strings (name or names if there are two more with the same value)

def get_oldest_person(table):
    '''Finds the oldest people

    Args:
        table:list of lists

    Returns:
        oldest_person: list of strings
    '''

    age = []
    for line in table:
        age.append(int(line[2]))
    oldest = min(age)

    oldest_person = []

    for lista in table:
        lista = tuple(lista)
        if int(lista[2]) == oldest:
            oldest_person.append(lista[1])

    return oldest_person


# the question: Who is the closest to the average age ?
# return type: list of strings (name or names if there are two more with the same value)
def get_persons_closest_to_average(table):
    '''Finds people with an age closest to the average

    Args:
        table: list of lists

    Returns:
        close_to_ave: list of strings

    '''
    average_age = []
    for line in table:
        average_age.append(int(line[2]))

    ave_numbers = 0

    for i in average_age:
        ave_numbers += i
        average = ave_numbers/len(average_age)

    year_delta = []

    for year in average_age:
        delta = year - average
        delta = abs(delta)
        year_delta.append(delta)
        mini = min(year_delta)

        close_to_ave = []
        index = 0

    for delta in year_delta:
        index += 1
        if delta == mini:
            index_ave = index-1
            close_to_ave.append(table[index_ave][1])

    return close_to_ave
