

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

    cell_widths = []
    columns = []

    for i in range(len(title_list)):
        columns.append([])
        for j in range(len(table)):
            columns[i].append(table[j][i])  # columns - nested list with lists of elements of table columns
        cell_widths.append(max(map(len, columns[i])))   # cell_widths - list with max len of str in table columns
    print(columns)
    print(cell_widths)

    width_of_table = -2
    for width in cell_widths:
        width_of_table += width     # sum of the longest string length from row in table
    print(width_of_table)
    '''
    row_to_print = '|'
    for i in range(len(title_list)):
        for j in range(len(table)):
            row_to_print += ' ' + ' '*round(cell_widths[i]-len(table[j][i])/2) + '{}' + ' '*round(cell_widths[i]-len(table[j][i])/2) + '|'
    '''
    row_to_print = '|'
    for i in range(len(table)):
        for j in range(len(title_list)):
            row_to_print += ' ' + ' '*round(cell_widths[j]-len(table[j][i])/2) + '{}' + ' '*round(cell_widths[j]-len(table[j][i])/2) + '|'

    print(row_to_print)

    print('/' + '-'*width_of_table + '\\')
    for row in table:
        print(row_to_print)
    print('\\' + '-'*width_of_table + '/')


# This function needs to print result of the special functions
#
# @result: string or list or dictionary - result of the special function
# @label: string - label of the result
def print_result(result, label):

    # your code

    pass


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
    inputs = []
    for i in range(len(list_labels)):
        inputs.append(input(list_labels[i]))
    return inputs


# This function needs to print an error message. (example: Error: @message)
#
# @message: string - the error message
def print_error_message(message):
    print(message)
