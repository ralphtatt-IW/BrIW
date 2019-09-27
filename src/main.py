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
    drinks = dbc.get_all_drinks()
    teams = dbc.get_all_teams()
    people = dbc.get_all_people(drinks, teams)
    rounds = dbc.get_all_rounds(people, teams)
    orders = dbc.get_all_orders(drinks, people, rounds)


    # If running as command line argument
    if len(arguments) > 1:

        if "get-people" in arguments:
            print(dbc.get_all_people())
            exit()

        if "get-drinks" in arguments:
            print(dbc.get_all_drinks())
            exit()

        if "get-teams" in arguments:
            print(dbc.get_all_teams())
            exit()

        if "get-rounds" in arguments:
            print(dbc.get_all_rounds())
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
            ui.help()

        if menu_option == 0:
            os.system("clear")
            print("Goodbye!")
            break


        input("Press ENTER to continue")
