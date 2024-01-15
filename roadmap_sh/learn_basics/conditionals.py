"""
Conditionals
Conditional Statements in Python perform different actions depending on whether a specific condition evaluates to true or false. Conditional Statements are handled by IF-ELIF-ELSE statements and MATCH-CASE statements in Python.

Visit the following resources to learn more:

Python Conditional Statements: IF…Else, ELIF & Switch Case
Conditional Statements in Python
How to use a match statement in Python
"""


# Why use a match case statement?
def file_handler_v1(command):
    match command.split():
        case ['show', *files]:
            print('List all files and directories: {}'.format(files))
            # code to list files
        case ['remove', *files]:
            print('Removing files: {}'.format(files))
            # code to remove files
        case _:
            print('Command not recognized')


commands = "remove"
file_handler_v1(commands)

file_handler_v1('show file1.txt file2.jpg file3.pdf')


def file_handler_v2(command):
    match command.split():
        case ['show']:
            print('List all files and directories: ')
            # code to list files
        case ['remove' | 'delete', *files] if '--ask' in files:
            del_files = [f for f in files if len(f.split('.')) > 1]
            print('Please confirm: Removing files: {}'.format(del_files))
            # code to accept user input, then remove files
        case ['remove' | 'delete', *files]:
            print('Removing files: {}'.format(files))
            # code to remove files
        case _:
            print('Command not recognized')


file_handler_v2('delete file1.txt file2')

