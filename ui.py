

# This function needs to print outputs like this:
# /-----------------------------------\
# |   id   |      title     |  type   |
# |--------|----------------|---------|
# |   0    | Counter strike |    fps  |
# |--------|----------------|---------|
# |   1    |       fo       |    fps  |
# \-----------------------------------/
#
# @table: list of lists - the table to print out
# @title_list: list of strings - the head of the table
def print_table(table, title_list):
    '''Prints given table with nice, smooth order and with centered values in cells.

    Args:
        table (nested list): table with data
        title_list (list of strings): list with titles of data in table

    Returns:
        None

    '''
    cell_widths = []
    columns = []
    SPACES_AROUND_STRING = 2

    for i in range(len(title_list)):
        columns.append([title_list[i]])
        for j in range(len(table)):
            columns[i].append(table[j][i])  # columns - nested list with lists of elements of table columns
        cell_widths.append(max(map(len, columns[i])))   # cell_widths - list with max len of str in table columns

    width_of_table = 0
    for width in cell_widths:
        width_of_table += width     # sum of the longest string length from row in table
    width_of_table += len(title_list) * SPACES_AROUND_STRING + len(title_list) + 1

    print('/' + '-' * (width_of_table-SPACES_AROUND_STRING) + '\\')
    row_to_print = '|'
    line_between_rows = '|'
    for i in range(len(table)+1):
        for j in range(len(title_list)):
            row_to_print += columns[j][i].center(cell_widths[j]+SPACES_AROUND_STRING) + '|'
            line_between_rows += '-'*(cell_widths[j]+SPACES_AROUND_STRING) + '|'
        print(row_to_print)
        if i == len(table):
            print('\\' + '-' * (width_of_table-SPACES_AROUND_STRING) + '/')
        else:
            print(line_between_rows)
            row_to_print = '|'
            line_between_rows = '|'


# This function needs to print result of the special functions
#
# @result: string or list or dictionary - result of the special function
# @label: string - label of the result
def print_result(result, label):
    '''Prints result of special functions in modules.

    Args:
        result: result from special function
        label: name of special function

    Returns:
        None

    '''
    print('\n\b', label, '\n')

    if type(result) in [str, float, int]:
        print(result)

    elif type(result) == list:
        for content in result:
            if type(content) == list:
                for inner_content in content:
                    print(inner_content, end=' ')
                print()
            else:
                print(content)

    elif type(result) == dict:
        longest_name = max(len(key) for key in result.keys())
        for key, value in result.items():
            print('{:{width}} {:3}'.format(key, value, width=longest_name))
    print('')


# This function needs to generate outputs like this:
# Main menu:
# (1) Store manager
# (2) Human resources manager
# (3) Inventory manager
# (4) Accounting manager
# (5) Selling manager
# (6) Customer relationship management (CRM)
# (0) Exit program
#
# @title: string - title of the menu
# @list_options: list of strings - the options in the menu
# @exit_message: string - the last option with (0) (example: "Back to main menu")
def print_menu(title, list_options, exit_message):
    '''Print menu with given parameters.

    Args:
        title (str): title of menu
        list_options (list): list_options with options of menu
        exit_message (str): message of exit menu or 'go-back' menu

    Returns:
        None

    '''
    print(title)
    for i in range(0, len(list_options)):
        print('({}) {}'.format(i+1, list_options[i]))
    print('(0)', exit_message)


# This function gets a list of inputs from the user by the terminal
#
# @list_labels: list of strings - the labels of the inputs
# @title: string - title of the "input section"
# @inputs: list of string - list of the received values from the user
def get_inputs(list_labels, title):
    '''Getting inputs from user.

    Args:
        list_labels (list): Labels of input(s).
        title (str): Title of input.

    Returns:
        inputs (list): List of inputs from user.

    '''
    inputs = []
    for i in range(len(list_labels)):
        inputs.append(input(list_labels[i]))
    return inputs


# This function needs to print an error message. (example: Error: @message)
#
# @message: string - the error message
def print_error_message(message):
    '''Prints given error message.

    Args:
        message (str): message with error

    Returns:
        None

    '''
    print(message)


def print_string(string):
    '''Prints given string.

    Args:
        string (str): string

    Returns:
        None

    '''
    print(string)
