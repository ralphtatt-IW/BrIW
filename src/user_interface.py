import os
import time
from prettytable import PrettyTable

DEFAULT_LENGTH = 43

# OUPUT
def print_in_line(s):
    print(s, end="")


def seperator(length):
    print_in_line("+")
    for x in range(length - 2):
        print_in_line("=")
    print("+")

# Centers text and makes uppercase
def header(s, length):
    spaces = length - len("| " + s + "|")
    print_in_line("| ")
    for i in range(int(spaces / 2)):
        print_in_line(" ")
    spaces += 1 if spaces % 2 == 1 else 0
    print_in_line(s.upper())
    for i in range(int(spaces / 2)):
        print_in_line(" ")
    print("|")


def row(s, length):
    # Amount of white space needed
    spaces = length - len("| " + s + "|")
    print_in_line("| ")
    print_in_line(s)
    for i in range(spaces):
        print_in_line(" ")
    print("|")


def print_table(name, data):
    if len(data) == 0:
        print(f"There is no data for {name}!")
        return

    tbl = PrettyTable()
    tbl.field_names = data[0].get_table_headers()

    for row in data:
        tbl.add_row(row.get_details())

    print(tbl)


def start_title():
    with open("files/title.txt", "r") as file:
        lines = file.read().splitlines()
    for i in range(0, len(lines) - 7):
        os.system("clear")
        seperator(DEFAULT_LENGTH)
        for j in range(0, 8):
            row(lines[i + j], DEFAULT_LENGTH)
        header("Now with pickle!", DEFAULT_LENGTH)
        seperator(DEFAULT_LENGTH)
        if i == 0:
            os.system("espeak -p 0 'Welcome to..'")
        time.sleep(.1)
    os.system("espeak -p 99 'brew, now with pickel' ")


def title():
    with open("files/title.txt", "r") as file:
        lines = file.read().splitlines()

    seperator(DEFAULT_LENGTH)
    for line in lines:
        if line.strip() != "":
            row(line, DEFAULT_LENGTH)
    header("Now with pickle!", DEFAULT_LENGTH)
    seperator(DEFAULT_LENGTH)


def print_menu():
    title()
    print("Options:")
    print("\t1. Add People")
    print("\t2. View People")
    print("")
    print("\t3. Add Drink")
    print("\t4. View Drinks")
    print("")
    print("\t5. Add Team")
    print("\t6. View Teams")
    print("")
    print("\t7. Start Round")
    print("\t8. View Active Rounds")
    print("\t9. View Completed Rounds")
    print("")
    print("\t10. Help")
    print("")
    print("\t0. Quit")
    seperator(DEFAULT_LENGTH)

def print_nuke():
    print("""     _.-^^---....,,--
 _--                  --_
<                        >)
|                         |
 \\._                   _./
    ```--. . , ; .--'''
          | |   |
       .-=||  | |=-.
       `-=#$%&%$#=-'
          | ;  :|
 _____.,-#%&$@%#&#~,._____
""")


def help():
    print("There is no help")

# INPUT
def get_int_input(limit):
    while True:
        option = input("Select Option $ ")

        if not option.isdigit():
            print("Not valid option!")
            continue

        if int(option) > limit or int(option) < 0:
            print(f"Must be between 0 and {limit}")
            continue

        return int(option)


def yes_or_no():
    while True:
        answer = input("Y/N?").lower()
        if 'y' == answer:
            return True
        if 'n' == answer:
            return False
        print("Not recognised")


def get_string_input(s):
    while True:
        string = input(s)
        if string != "":
            return string
        print("Can not be empty")

if __name__ == "__main__":
    print("Why are you running this as main?")
