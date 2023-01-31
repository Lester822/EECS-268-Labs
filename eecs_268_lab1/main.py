from executive import Executive


def main():
    file_name = input('Enter the name of the input file: ')
    my_exec = Executive(file_name)
    my_exec.run()


if __name__ == '__main__':
    main()