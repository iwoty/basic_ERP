# implement commonly used functions here

import random


# generate and return a unique and random string
# other expectation:
# - at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter
# - it must be unique in the list
#
# @table: list of list
# @generated: string - generated random string (unique in the @table)

table = []
special_char = ['!','@', '#', '$', '%', '^', '&', '*', '(', ')', '?']
def generate_random(table):
    generated = ''
    # chr(random.randint(97, 122)) # a - z
    # chr(random.randint(65, 90)) # A - Z
    # chr(random.randint(48, 57)) # 1 - 9
    # random.choice(special_char)

    generated = (chr(random.randint(97, 122)) + chr(random.randint(65, 90)) + chr(random.randint(48, 57)) + chr(random.randint(48, 57)) + chr(random.randint(65, 90)) + chr(random.randint(97, 122)) + random.choice(special_char) + random.choice(special_char))
    for item in table:
        while generated == table[0]:
            generated = (chr(random.randint(97, 122)) + chr(random.randint(65, 90)) + chr(random.randint(48, 57)) + chr(random.randint(48, 57)) + chr(random.randint(65, 90)) + chr(random.randint(97, 122)) + random.choice(special_char) + random.choice(special_char))

    return generated

generate_random(table)