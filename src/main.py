#! /usr/bin/env python3
from classes import *
import user_interface as ui
from functions import *

from prettytable import PrettyTable
import pickle
import os
import sys

arguments = sys.argv

# Loading data to file
people = load_file_to_data("people")
drinks = load_file_to_data("drinks")
rounds = load_file_to_data("rounds")
teams = load_file_to_data("teams")
completed_rounds = load_file_to_data("completed_rounds")

# If running as command line argument
if len(arguments) > 1:

    if "get-people" in arguments:
        printing.print_table("People", people)
        exit()

    if "get-drinks" in arguments:
        printing.print_table("Drinks", drinks)
        exit()

    if "get-preferences" in arguments:
        print_preferences()
        exit()

    if "easter-egg" in arguments:
        printing.start_credits()
        exit()

    if "nuke-data" in arguments:
        print("Are you sure you want to delete all data?")

        if ui.yes_or_no():
            save_data_to_file(people, "people_back_up")
            save_data_to_file(drinks, "drinks_back_up")
            save_data_to_file(rounds, "rounds_back_up")
            save_data_to_file(teams, "teams_back_up")
            save_data_to_file(completed_rounds, "completed_rounds_back_up")
            save_data_to_file([], "people")
            save_data_to_file([], "drinks")
            save_data_to_file([], "rounds")
            save_data_to_file([], "teams")
            save_data_to_file([], "completed_rounds")
            print("Data nuked and backed up!")

        exit()

    print("Command not recognised")
    exit()

# System Start
# ui.start_title()

while True:

    os.system("clear")

    ui.print_menu()

    menu_option = ui.get_int_input(9)

    if menu_option == 1:
        os.system("clear")
        add_person()

    if menu_option == 2:
        os.system("clear")
        view_people()

    if menu_option == 3:
        os.system("clear")
        add_drink()

    if menu_option == 4:
        os.system("clear")
        view_drinks()

    if menu_option == 5:
        os.system("clear")
        add_team()

    if menu_option == 6:
        os.system("clear")
        view_teams()

    if menu_option == 7:
        os.system("clear")
        start_round()

    if menu_option == 8:
        os.system("clear")
        view_rounds()

    if menu_option == 9:
        os.system("clear")
        view_completed_rounds()

    if menu_option == 10:
        ui.help()

    if menu_option == 0:
        os.system("clear")
        print("Goodbye!")
        break

    if menu_option == 142857:
        os.system("clear")
        debug()

    for round in rounds:
        if not round.active:
            rounds.remove(round)
            completed_rounds.append(round)
    save_all()


    input("Press ENTER to continue")
