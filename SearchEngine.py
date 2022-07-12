import re


def open_file(filename):
    global file
    file = open('dictionary/dictionary.txt', 'r')


# start
def load_dictionary():
    current_key = 'none'
    defn = ""
    global dictionary
    dictionary = dict()
    dictionary[current_key] = ''
    for i, line in enumerate(file):
        if line.isupper():
            current_key = line.strip()
            dictionary[current_key] = ''
        if len(line.strip()) != 0:
            dictionary[current_key] = dictionary[current_key] + ' ' + line


# end


def search_in_dictionary(query):
    print(dictionary[query.strip().upper()])


def close_opened_file():
    global file
    file.close()


def main():
    open_file('dictionary/dictionary.txt')
    load_dictionary()
    query = input('Enter the query: ')
    search_in_dictionary(query)
    close_opened_file()


main()
