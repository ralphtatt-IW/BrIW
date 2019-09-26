#! /usr/bin/env python3
from classes import *
import file_management as fm
import user_interface as ui
from functions import *
import database_connect as dbc

import pymysql
from prettytable import PrettyTable
import os
import sys

if __name__ == "__main__":

    arguments = sys.argv

    # Loading data to file
    people = fm.load_file_to_data("people")
    drinks = fm.load_file_to_data("drinks")
    rounds = fm.load_file_to_data("rounds")
    teams = fm.load_file_to_data("teams")
    completed_rounds = fm.load_file_to_data("completed_rounds")


    # If running as command line argument
    if len(arguments) > 1:

        if "get-people" in arguments:
            ui.print_table("People", people)
            exit()

        if "get-drinks" in arguments:
            print(dbc.get_all_drinks())
            exit()

        if "get-teams" in arguments:
            print(dbc.get_all_teams())
            exit()

        if "get-rounds" in arguments:
            ui.print_table("Rounds", rounds)
            exit()

        if "nuke-data" in arguments:
            print("Are you sure you want to delete all data?")

            if ui.yes_or_no():
                fm.nuke_data(people, drinks, teams, rounds, completed_rounds)
                ui.print_nuke()
                print("Data nuked!")

            exit()
        if "-f" not in arguments:
            print("Command not recognised")
            exit()
        else:
            # System Start
            ui.start_title()

    while True:

        os.system("clear")

        ui.print_menu()
        menu_option = ui.get_int_input(10)



        if menu_option == 1:
            os.system("clear")
            person_option(people, teams, drinks)

        if menu_option == 2:
            os.system("clear")
            view_people(people)

        if menu_option == 3:
            os.system("clear")
            drink_option(drinks)

        if menu_option == 4:
            os.system("clear")
            view_drinks(drinks)

        if menu_option == 5:
            os.system("clear")
            team_option(teams)

        if menu_option == 6:
            os.system("clear")
            view_teams(teams)

        if menu_option == 7:
            os.system("clear")
            round_option(rounds, people)

        if menu_option == 8:
            os.system("clear")
            view_rounds(rounds, people, drinks)

        if menu_option == 9:
            os.system("clear")
            view_completed_rounds(completed_rounds)

        if menu_option == 10:
            ui.help()

        if menu_option == 0:
            os.system("clear")
            print("Goodbye!")
            break

        update_rounds(rounds, completed_rounds)

        input("Press ENTER to continue")
        fm.save_all(people, drinks, teams, rounds, completed_rounds)
