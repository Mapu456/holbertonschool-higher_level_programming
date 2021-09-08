#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for arguments in dir(hidden_4):
        if arguments[0:2] != '__':
            if arguments[0:12] == "print_hidden":
                print("print_holberton")
            else:
            	print("{:s}".format(arguments))
