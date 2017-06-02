# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# title: string
# manufacturer: string
# price: number (dollar)
# in_stock: number


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
    table = data_manager.get_table_from_file('store/games.csv')
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
        manufacturer_count = get_counts_by_manufacturers(table)
        ui.print_result(manufacturer_count, 'Name of manufacturers : amount of products')
    elif option == "6":
        manufacturer = ''.join(ui.get_inputs(['Enter a manufacturer: '], ''))
        average = get_average_by_manufacturer(table, manufacturer)
        ui.print_result(average, ('Average amount of games in stock by ' + manufacturer))

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
               "How many different kinds of game are available of each manufacturer?",
               "What is the average amount of games in stock of a given manufacturer?"]

    ui.print_menu("----> Store manager", options, "Go back to the main menu")


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
    title_list = ['id', 'title', 'manufacturer', 'price', 'in_stock']
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
    list_labels = ['Enter title: ',
                   'Enter manufacturer: ',
                   'Enter price: ',
                   'In_stock: ']
    inputs = [common.generate_random(table)]
    inputs += ui.get_inputs(list_labels, '')
    table.append(inputs)
    data_manager.write_table_to_file('store/games.csv', table)
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
    data_manager.write_table_to_file('store/games.csv', table)
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

    list_labels = ['Enter title: ',
                   'Enter manufacturer: ',
                   'Enter price: ',
                   'In_stock: ']
    inputs = [id_to_keep]
    inputs += ui.get_inputs(list_labels, '')
    table.append(inputs)
    data_manager.write_table_to_file('store/games.csv', table)
    return table


# special functions:
# ------------------

# the question: How many different kinds of game are available of each manufacturer?
# return type: a dictionary with this structure: { [manufacturer] : [count] }
def get_counts_by_manufacturers(table):
    '''
    Parameters
    ----------
    table : list

    Returns
    -------
    manufacturer_count : dictionary { [manufacturer] : [count] }

    '''
    manufacturer_count = {}

    for manufacturer in table:
        if manufacturer[2] in manufacturer_count:
            manufacturer_count[manufacturer[2]] += 1
        else:
            manufacturer_count[manufacturer[2]] = 1

    return manufacturer_count


# the question: What is the average amount of games in stock of a given manufacturer?
# return type: number
def get_average_by_manufacturer(table, manufacturer):
    '''
    Parameters
    ----------
    table : list

    Returns
    -------
    manufacturer_count : dictionary { [manufacturer] : [count] }

    '''
    counter = 0
    amount_in_shop = 0

    for product in table:
        if product[2].upper() == manufacturer.upper():
            counter += 1
            amount_in_shop = amount_in_shop + int(product[4])

    if counter == 0:
        average = 'There is no ' + manufacturer + ' in table records '
    else:
        average = amount_in_shop / counter

    return average
