import datetime


def open_file(filename):
    create_log(f'Opening file {filename}.')
    global file
    file = open('dictionary/dictionary.txt', 'r')
    create_log(f'Done opening file {filename}.')


# start
def load_dictionary():
    create_log("Loading the data from dictionary.txt into dictionary data structure.")
    # current_key holds the current keyword in the dictionary.
    current_key = 'none'
    global dictionary
    dictionary = dict()
    dictionary[current_key] = ''
    # Reading the file through enumerate.
    for i, line in enumerate(file):
        # The keywords are all in Uppercase and so the condition.
        if line.isupper():
            current_key = line.strip()
            dictionary[current_key] = ''
        # This condition is to check if the line is empty.
        if len(line.strip()) != 0:
            # Appending the value into the dictionary DS.
            dictionary[current_key] = dictionary[current_key] + ' ' + line
    create_log("Done loading the data from dictionary.txt into dictionary data structure.")


# end


def search_in_dictionary(query):
    create_log(f'Searching "{query}" from the dictionary data structure.')
    # If the query is present print it. Else the KeyError is handled for definition not found.
    try:
        definition_of_query = dictionary[query.strip().upper()]
        create_log(f'The entered query\'s "{query}" definition found and printing it.')
        print(definition_of_query)
    except KeyError:
        print(f'The entered query\'s "{query}" definition not found.')
        create_log(f'The entered query\'s "{query}" definition not found.')


def close_opened_file():
    global file
    create_log(f'Closing the opened file.')
    file.close()
    create_log(f'Done closing the opened file.')


def create_log(data):
    global log
    log = open("logs.txt", "a")
    log.write(str(datetime.datetime.now()) + "\t" + data + "\n")


def main():
    open_file('dictionary/dictionary.txt')
    load_dictionary()
    create_log('Taking query input from user.')
    query = input('Enter the query: ')
    create_log(f'The query entered by the user is {query}.')
    search_in_dictionary(query)
    close_opened_file()


main()
