#! /usr/bin/env python3
from classes import *
import user_interface as ui

from prettytable import PrettyTable
import pickle
import os
import sys

def save_data_to_file(data, filename):
    with open(f"files/{filename}.pickle", 'wb') as handle:
        pickle.dump(data, handle)


def load_file_to_data(filename):
    try:
        with open(f"files/{filename}.pickle", 'rb') as handle:
            data = pickle.load(handle)
        return data
    except:
        return []


def save_all():
    save_data_to_file(people, "people")
    save_data_to_file(drinks, "drinks")
    save_data_to_file(teams, "teams")
    save_data_to_file(rounds, "rounds")
    save_data_to_file(completed_rounds, "completed_rounds")


def add_person():
    if len(teams) == 0:
        print("Add a team option first")
        return

    if len(drinks) == 0:
        print("Add a drink option first")
        return

    print("Adding new Person...")
    # Get details
    f_name = ui.get_string_input("What is their first name? $")
    l_name = ui.get_string_input("What is their surname? $")

    # Add team?
    print("Select team: (Add team on main menu if it doesn't exist)")
    team_index = choose_option_from_list(teams)
    if team_index == -1:
        return
    else:
        team = teams[team_index]

    # Add Favourite Drink
    print("Select Drink: (Add drink on main menu if it doesn't exist)")
    drink_index = choose_option_from_list(drinks)
    if drink_index == -1:
        return
    else:
        pref = drinks[drink_index]

    new_person = Person(f_name, l_name, pref, team)

    # Add to list
    people.append(new_person)
    print("Person added!")


def add_drink():
    print("Adding new drink...")
    drink_name = ui.get_string_input("Enter drink name $")

    new_drink = Drink(drink_name)
    drinks.append(new_drink)
    save_data_to_file(drinks, "drinks")


def add_team():
    print("Adding new team...")
    team_name = ui.get_string_input("Enter team name $")
    team_location = ui.get_string_input("Enter location $")

    new_team = Team(team_name, team_location)
    teams.append(new_team)


def view_people():
    ui.print_table("People", people)


def view_drinks():
    ui.print_table("Drinks", drinks)


def view_teams():
    ui.print_table("Teams", teams)


def choose_option_from_list(list):
    index = 1

    for item in list:
        print(f"{index}. {item}")
        index += 1

    print("0. Cancel")

    return ui.get_int_input(index - 1) - 1


def start_round():
    if len(people) == 0:
        print("There is no one to make a round")
        return

    print("Who is making the round?")

    maker_index = choose_option_from_list(people)
    if maker_index == -1:
        return

    new_round = Round(people[maker_index], people[maker_index].get_team())

    print(f"Round being made by {new_round.get_maker()}")
    rounds.append(new_round)


def add_to_round(round):
    while True:
        person_choice = choose_option_from_list(people)

        if person_choice == -1:
            return
        person = people[person_choice]

        if person.get_team() != round.get_maker().get_team():
            print(id(person.get_team()))
            print(id(round.get_maker().get_team()))
            print("Can only accept orders from same team!")
            continue

        break

    if person.get_preference() != None:
        print(f"Is the order {person.get_preference()}?")
        if ui.yes_or_no():
            new_order = Order(person, person.get_preference())
            round.add_order(new_order)
            return

    print("Choose drink from list")
    drink_choice = choose_option_from_list(drinks)
    new_order = Order(person, drinks[drink_choice])
    round.add_order(new_order)


def view_rounds():
    ui.print_table("Rounds", rounds)
    if len(rounds) == 0:
        return
    print("Would you like to see details of a round?")
    user_choice = choose_option_from_list(rounds)
    if user_choice == -1:
        return
    round_details(rounds[user_choice])


def round_details(round):
    os.system("clear")
    print(round)
    ui.print_table("Orders", round.orders)
    print("Options:")
    print("\t1. Add to Order")
    print("\t2. Mark Completed")
    print("\t3. Change Maker")
    print("\t0. Return")
    menu_option = ui.get_int_input(3)

    if menu_option == 1:
        add_to_round(round)
    if menu_option == 2:
        round.finish_round()
    if menu_option == 3:
        print("Not implemented")
    if menu_option == 0:
        return


def view_completed_rounds():
    ui.print_table("Old Rounds", completed_rounds)


def debug():
    print("DEBUG MODE")
    print("to be implemented")


def nuke_data():
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


if __name__ == "__main__":

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
            ui.print_table("People", people)
            exit()

        if "get-drinks" in arguments:
            ui.print_table("Drinks", drinks)
            exit()

        if "get-teams" in arguments:
            ui.print_table("Teams", teams)
            exit()

        if "get-rounds" in arguments:
            ui.print_table("Rounds", rounds)
            exit()

        if "nuke-data" in arguments:
            print("Are you sure you want to delete all data?")

            if ui.yes_or_no():
                nuke_data()
                print("Data nuked and backed up!")

            exit()

        print("Command not recognised")
        exit()

    # System Start
    #ui.start_title()

    while True:

        os.system("clear")

        ui.print_menu()

        menu_option = ui.get_int_input(10)

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
