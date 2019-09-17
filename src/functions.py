import user_interface as ui
from classes import *
import os


def check_empty(data):
    return len(data) == 0

def list_options(list):
    index = 1

    for item in list:
        print(f"{index}. {item}")
        index += 1

    print("0. Cancel")


def choose_option_from_list(list):
    list_options(list)

    return ui.get_int_input(len(list)) - 1


def view_people(people):
    ui.print_table("People", people)


def view_drinks(drinks):
    ui.print_table("Drinks", drinks)


def view_teams(teams):
    ui.print_table("Teams", teams)


def add_person(f_name, l_name, pref, team, people):
    new_person = Person(f_name, l_name, pref, team)
    # Add to list
    people.append(new_person)


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
    team_index = choose_option_from_list(teams)
    if team_index == -1:
        return

    team = teams[team_index]

    # Add Favourite Drink
    print("Select Drink: (Add drink on main menu if it doesn't exist)")
    drink_index = choose_option_from_list(drinks)
    if drink_index == -1:
        return

    pref = drinks[drink_index]

    add_person(f_name, l_name, pref, team, people)
    print(f"{f_name} added!")


def add_drink(drink_name, drinks):
    new_drink = Drink(drink_name)
    drinks.append(new_drink)


def drink_option(drinks):
    print("Adding new drink...")
    drink_name = ui.get_string_input("Enter drink name $")

    add_drink(drink_name, drinks)


def add_team(team_name, team_location, teams):
    new_team = Team(team_name, team_location)
    teams.append(new_team)


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

    maker_index = choose_option_from_list(people)

    if maker_index == -1:
        return


    round_maker = people[maker_index]
    round_team = round_maker.get_team()

    add_round(round_maker, round_team, rounds)

    print(f"Round being made by {round_maker}")


def add_round(round_maker, round_team, rounds):
    new_round = Round(round_maker, round_team)
    rounds.append(new_round)


def add_order_to_round(round, people, drinks):
    while True:
        person_choice = choose_option_from_list(people)

        if person_choice == -1:
            return

        person = people[person_choice]

        if person.get_team() != round.get_maker().get_team():
            print("Can only accept orders from same team!")
            continue

        break


    print(f"Is the order {person.get_preference()}?")
    if ui.yes_or_no():
        new_order = Order(person, person.get_preference())
        round.add_order(new_order)
        return

    print("Choose drink from list")
    drink_choice = choose_option_from_list(drinks)
    new_order = Order(person, drinks[drink_choice])
    round.add_order(new_order)


def view_rounds(rounds, people, drinks):
    ui.print_table("Rounds", rounds)
    if len(rounds) == 0:
        return
    print("Would you like to see details of a round?")
    user_choice = choose_option_from_list(rounds)
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


def update_rounds(rounds, completed_rounds):
    for round in rounds:
        if not round.active:
            rounds.remove(round)
            completed_rounds.append(round)


def view_completed_rounds(completed_rounds):
    ui.print_table("Old Rounds", completed_rounds)
