FILEPATH = "quote.txt"


def get_quote(filepath=FILEPATH):

    with open(filepath, 'r') as monday_quote:
        today_quote = monday_quote.readlines()
    return today_quote

"""
def write_balance(todos_arg, filepath=FILEPATH):
    #Write the to-do items list in the text file.
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
"""