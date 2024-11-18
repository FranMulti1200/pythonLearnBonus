FILEPATH = "current_balance.txt"


def get_balance(filepath=FILEPATH):

    with open(filepath, 'r') as balance_local:
        actual_balance = balance_local.readline()
    return actual_balance

def write_balance(todos_arg, filepath=FILEPATH):
    """ Write the to-do items list in the text file. """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)