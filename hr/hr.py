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
    while True:
        handle_menu()
        try:
            if choose() == 'back_to_main':
                break
        except KeyError as err:
            ui.print_error_message(err)


def choose():
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

    # your code

    pass


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

# the question: Who is the oldest person ?
# return type: list of strings (name or names if there are two more with the same value)
def get_oldest_person():
    """
    table = data_manager.get_table_from_file('hr/persons.csv')
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
    """
    pass



    #print(oldest)
    """age = {}
    for lista in table:
        key = lista[2]
        key = int(key)
        value = lista[1]
        age[key] = value
    print(age)
    oldest = min(age.keys())
    print(age.keys())
    old = []
    for year in age.keys():
        if year == oldest:
            old.append(age[year])
    print(old)"""



    #age.values() =
    #table = bubble_sort(age.values())
    """oldest = []
    for i in table:
        if table[0] == table[i]:
            oldest.append(table[i])
    print(old)"""


    #return old





# the question: Who is the closest to the average age ?
# return type: list of strings (name or names if there are two more with the same value)
def get_persons_closest_to_average(table):

    # your code

    pass

#get_oldest_person()
#print(bubble_sort(tab))
