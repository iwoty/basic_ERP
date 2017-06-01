# implement commonly used functions here

import random


# generate and return a unique and random string
# other expectation:
# - at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter
# - it must be unique in the list
#
# @table: list of list
# @generated: string - generated random string (unique in the @table)


def generate_random(table):
    '''Checking if generated id is unique

    Args:
        table (nested list): table for check if generated key is not already in table

    Returns:
        unique_id (str): generated unique id

    '''
    unique_id = genrate_id()

    for product_id in table:
        while unique_id == product_id[0]:
            unique_id = genrate_id()

    return unique_id


def genrate_id():
    '''Generating random id number

    Returns:
        generated (str): generated key

    '''

    FROM_a_TO_z = ['a',	'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',	'j', 'k', 'l', 'm',	'n', 'o', 'p', 'q',	'r', 's', 't', 'u',	'v', 'w', 'x', 'y', 'z']
    FROM_A_TO_Z = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    FROM_0_TO_9 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    SPECIAL_CHAR = ['!', '@', '#', '$', '%', '&',]

    generated = []

    generated.append(random.choice(FROM_a_TO_z))
    generated.append(random.choice(FROM_A_TO_Z))
    generated.append(random.choice(FROM_0_TO_9))
    generated.append(random.choice(FROM_0_TO_9))
    generated.append(random.choice(FROM_A_TO_Z))
    generated.append(random.choice(FROM_a_TO_z))
    generated.append(random.choice(SPECIAL_CHAR))
    generated.append(random.choice(SPECIAL_CHAR))

    generated_id = ''.join(generated)

    return generated_id


def str_to_int_in(table):
    '''Change last two elements of nested list from string to integer

    Args:
        table (nested list): table with records

    Returns:
        table (nested list): filtrated table
    '''

    for sign in table:
        sign[-1] = int(sign[-1])
        sign[-2] = int(sign[-2])

    return table