import pickle

def save_data_to_file(data, filename):
    with open(f"files/{filename}.pickle", 'wb') as handle:
        pickle.dump(data, handle)


def load_file_to_data(filename):
    with open(f"files/{filename}.pickle", 'rb') as handle:
        data = pickle.load(handle)
    return data


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
    print("Add team?")
    add_team = ui.yes_or_no()

    # List teams todo
    if add_team:
        team_index = choose_option_from_list(teams)
        if team_index == -1:
            add_team == False
        else:
            team = teams[team_index]

    # Add Favourite Drink
    print("Add drink preference?")
    add_pref = ui.yes_or_no()

    # List Drinks todo
    if add_pref:
        print("Select drink from list:")

        drink_index = choose_option_from_list(drinks)
        if drink_index == -1:
            add_pref = False
        else:
            pref = drinks[drink_index]

    if add_pref:
        if add_team:
            new_person = Person(f_name, l_name, pref, team)
        else:
            new_person = Person(f_name, l_name, pref, None)
    else:
        if add_team:
            new_person = Person(f_name, l_name, None, team)
        else:
            new_person = Person(f_name, l_name)

    # Add to list
    people.append(new_person)
    save_data_to_file(people, "people")
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

    return ui.get_int_input(len(list) + 1) - 1


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
    save_data_to_file(rounds, "rounds")


def add_to_round(round):
    person_choice = choose_option_from_list(people)
    if person_choice == -1:
        return
    person = people[person_choice]
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
