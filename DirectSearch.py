def open_file(filename):
    global file
    file = open('dictionary/dictionary.txt', 'r')


def close_opened_file():
    global file
    file.close()


def search_query(query):
    line_of_query = 0
    defn = ""
    line_found = False
    for i, line in enumerate(file):
        # if query.upper() in line:
        if line.startswith(query.upper()):
            print(line)
            line_of_query = i
            line_found = True
        if line_found:
            break
    defn_found = False
    open_file('dictionary/dictionary.txt')
    for i, line in enumerate(file):
        if i > line_of_query:
            if "Defn: " or '1. ' in line:
                defn_found = True
                defn = line.strip()
                # print(defn)
            if line.isupper():
                exit(0)
            elif defn_found:
                defn = line.strip()
                print(defn)
        # if defn_found:
        #     break


def main():
    open_file('dictionary/dictionary.txt')
    query = input("Enter the query: ")
    search_query(query)
    close_opened_file()


main()
