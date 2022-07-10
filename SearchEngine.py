def open_file(filename):
    global file
    file = open('dictionary/dictionary.txt', 'r')


def search_query(query=''):
    global file
    count = 0
    key = list()
    for data in file.readlines():
        if data.isupper():
            key.append(data.strip())
    print(key)
    for i in range(30, 50):
        print(key[i], end=" ")


def add_into_dict():
    dictionary = dict()
    for data in file.readlines():
        if data.isupper():
            dictionary[data] = defn


def main():
    open_file('dictionary/dictionary.txt')
    # query = input('Enter the query: ')
    # search_query(query)
    search_query()
    # add_into_dict()


main()
