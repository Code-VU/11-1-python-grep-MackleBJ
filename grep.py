import re
import string
import sys


def countpatterninfile():
    regular_expression = input("Enter a regular expression: ")
    file_handle = open('mbox-long.txt','r')

    matches_found = 0
    for line in file_handle:
        matching_portion = re.findall(regular_expression, line)
        if len(matching_portion) > 0:
            matches_found += 1

    print('mbox.txt had {} lines that matched {}'.format(matches_found, regular_expression))

if __name__ == '__main__':
    # this is called a main method
    # This is another way of telling python THIS IS WHERE YOU SHOULD START RUNNING
    # When this is included, python will begin with the code in this block first
    countpatterninfile()