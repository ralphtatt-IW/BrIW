import user_interface as ui
from classes import *
import os
import database_connect as dbc


def check_empty(data):
    return len(data) == 0


def list_options(dict):
    index = 1

    for item in list(dict.values()):
        print(f"{index}. {item}")
        index += 1

    print("0. Cancel")


def choose_key_from_dict(d):
    list_options(d)
    option_chosen = ui.get_int_input(len(d)) - 1
    if option_chosen == -1:
        return -1
    key = list(d.keys())[option_chosen]
    return key


def view_people(people):
    ui.print_table("People", people)


def view_drinks(drinks):
    ui.print_table("Drinks", drinks)


def view_teams(teams):
    ui.print_table("Teams", teams)


def add_person(f_name, l_name, pref, team, people={}):
    id = dbc.get_fresh_id("People", "person_id")
    new_person = Person(id, f_name, l_name, team, pref)
    # Add to list
    dbc.save_person(new_person)
    people[id] = new_person

# Adding a new person


def person_option(people, teams, drinks):
    if check_empty(teams):
        print("Add a team option first")
        return

    if check_empty(drinks):
        print("Add a drink option first")
        return

    print("Adding new Person...")
    # Get details
    f_name = ui.get_string_input("What is their first name? $")
    l_name = ui.get_string_input("What is their surname? $")

    # Add team?
    print("Select team: (Add team on main menu if it doesn't exist)")
    team_key = choose_key_from_dict(teams)
    if team_key == -1:
        return

    team = teams[team_key]

    # Add Favourite Drink
    print("Select Drink: (Add drink on main menu if it doesn't exist)")
    drink_key = choose_key_from_dict(drinks)
    if drink_key == -1:
        return

    pref = drinks[drink_key]

    add_person(f_name, l_name, pref, team, people)
    print(f"{f_name.capitalize()} added!!")


def add_drink(drink_name, drinks={}):
    id = dbc.get_fresh_id("Drinks", "drink_id")
    new_drink = Drink(id, drink_name)
    dbc.save_drink(new_drink)
    drinks[id] = new_drink


def drink_option(drinks):
    print("Adding new drink...")
    drink_name = ui.get_string_input("Enter drink name $")

    add_drink(drink_name, drinks)


def add_team(team_name, team_location, teams={}):
    id = dbc.get_fresh_id("Teams", "team_id")

    new_team = Team(id, team_name, team_location)

    teams[id] = new_team
    dbc.save_team(new_team)


def team_option(teams):
    print("Adding new team...")
    team_name = ui.get_string_input("Enter team name $")
    team_location = ui.get_string_input("Enter location $")

    add_team(team_name, team_location, teams)


def round_option(rounds, people):
    if check_empty(people):
        print("There is no one to make a round")
        return

    print("Who is making the round?")

    maker_key = choose_key_from_dict(people)

    if maker_key == -1:
        return

    round_maker = people[maker_key]
    round_team = round_maker.get_team()

    add_round(round_maker, round_team, rounds)

    print(f"Round being made by {round_maker}")


def add_round(round_maker, round_team, rounds={}):
    id = dbc.get_fresh_id("Rounds", "round_id")

    new_round = Round(id, round_maker, True, round_team)

    rounds[id] = new_round
    dbc.save_round(new_round)


def choose_person_for_order(round, people):
    while True:
        person_choice = choose_key_from_dict(people)

        if person_choice == -1:
            return

        person = people[person_choice]

        if person.get_team() != round.get_maker().get_team():
            print("Can only accept orders from same team!")
            continue

        return person

def add_order(person, drink, round, notes=""):
    id = dbc.get_fresh_id("Orders", "order_id")
    new_order = Order(id, person, drink, round.round_id, notes)
    dbc.save_order(new_order)
    round.add_order(new_order)

def add_order_to_round(round, people, drinks):
    person = choose_person_for_order(round, people)

    print(f"Is the order {person.get_preference()}?")
    if ui.yes_or_no():
        new_order = Order(person, person.get_preference())
        round.add_order(new_order)
        return

    print("Choose drink from list")

    drink_key = choose_key_from_dict(drinks)
    if drink_key == -1:
        return -1

    add_order(person, drinks[drink_key], round )


def view_rounds(rounds, people, drinks):
    ui.print_table("Rounds", rounds)
    if len(rounds) == 0:
        return
    print("Would you like to see details of a round?")
    user_choice = choose_key_from_dict(rounds)
    if user_choice == -1:
        return
    round_details(rounds[user_choice], people, drinks)


def round_details(round, people, drinks):
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
        add_order_to_round(round, people, drinks)
    if menu_option == 2:
        round.finish_round()
    if menu_option == 3:
        print("Not implemented")
    if menu_option == 0:
        return
