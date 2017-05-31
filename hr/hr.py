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
    '''???

    Args:
        param1: ???
        param2: ???

    Returns:
        ?????

    '''
    while True:
        handle_menu()
        try:
            if choose() == 'back_to_main':
                break
        except KeyError as err:
            ui.print_error_message(err)


def choose():
    '''???

    Args:
        param1: ???
        param2: ???

    Returns:
        ?????

    '''
    table = data_manager.get_table_from_file('hr/persons.csv')
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
        get_oldest_person(table)
    elif option == "6":
        get_persons_closest_to_average(table)
    elif option == "0":
        return 'back_to_main'
    else:
        raise KeyError("There is no such option.")


def handle_menu():
    '''???

    Args:
        param1: ???
        param2: ???

    Returns:
        ?????

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
    '''???

    Args:
        param1: ???
        param2: ???

    Returns:
        ?????

    '''
    title_list = ['id', 'name', 'birth_date']
    ui.print_table(table, title_list)


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):
    '''???

    Args:
        param1: ???
        param2: ???

    Returns:
        ?????

    '''
    # your code

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

# the question: Who is the oldest person ?
# return type: list of strings (name or names if there are two more with the same value)

def get_oldest_person(table):
    '''???

    Args:
        param1: ???
        param2: ???

    Returns:
        ?????
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
    '''???

    Args:
        param1: ???
        param2: ???

    Returns:
        ?????

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

<<<<<<< HEAD
=======

def bubble_sort(numbers):
    '''???

    Args:
        param1: ???
        param2: ???

    Returns:
        ?????

    '''
    amount = len(numbers)-1
    for step in range(0, amount):
        replacement = True
        for index in range(0, amount-step):
            if numbers[index] > numbers[index+1]:
                numbers[index], numbers[index+1] = numbers[index+1], numbers[index]
                replacement = False
        if replacement:
            return numbers
>>>>>>> 84f355dedffa8fa7c6eed77363f6ead317c2ce57
