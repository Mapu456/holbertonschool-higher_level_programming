#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for arguments in dir(hidden_4):
        if arguments[0:1] != '_':
            print(arguments)
