def display_file(file):
    file.read()


def main():
    file = open('dictionary/dictionary.txt', 'r')
    str = file.read();
    print(len(str))
    #print(str)


def open_file(file):
    file = open('dictionary/dictionary.txt', 'r')
    str = file.read(3);
    print(str)


main()
