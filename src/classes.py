class Person:
    # name
    def __init__(self, person_id, first_name, second_name, team, preference):
        self.person_id = person_id
        self.first_name = first_name
        self.second_name = second_name
        self.full_name = first_name + " " + second_name
        self.second_name = second_name
        self.preference = preference
        self.team = team

    def __str__(self):
        return f"{self.full_name} ({self.team})"

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def get_name(self):
        return self.full_name

    def get_preference(self):
        return self.preference

    def get_team(self):
        return self.team

    def get_rounds_made(self):
        return self.rounds_made

    def get_table_headers(self):
        return ["Name", "Team Name", "Fav. Drink"]

    def get_details(self):
        return [self.get_name(), self.get_team(), self.get_preference()]

    def set_preference(self, preference):
        self.preference = preference


class Drink:
    def __init__(self, drink_id, name):
        self.drink_id = drink_id
        self.name = name

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.drink_id == other.drink_id

    def get_table_headers(self):
        return ["Name"]

    def get_details(self):
        return [self.name]


class Team:
    def __init__(self, team_id, name, location):
        self.team_id = team_id
        self.name = name
        self.location = location

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.team_id == other.team_id

    def get_table_headers(self):
        return ["Name", "Location"]

    def get_details(self):
        return [self.name, self.location]


# A teams order is added to a round
class Round:
    def __init__(self, round_id, maker, active, team):
        self.round_id = round_id
        self.maker = maker
        self.orders = {}
        self.active = active
        self.team = team

    def __str__(self):
        return f"Team:{self.team} - Maker:{self.maker.get_name()}"

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def get_maker(self):
        return self.maker

    def add_order(self, order):
        self.orders[order.order_id] = order

    def get_team(self):
        return self.team

    def finish_round(self):
        self.active = False

    def get_table_headers(self):
        return ["Team Name", "Maker", "Active"]

    def get_details(self):
        return [self.get_team(), self.get_maker(), self.active]

# User makes an order for a drink
class Order:
    def __init__(self, order_id, person, drink, round_id, notes=None):
        self.order_id = order_id
        self.person = person
        self.drink = drink
        self.notes = notes
        self.round_id = round_id

    # def change_order(self, new_drink):
    #     self.drink = new_drink
    #

    def get_table_headers(self):
        return ["Person", "Drink", "Notes"]

    def get_notes(self):
        return self.notes

    def get_details(self):
        return [self.person, self.drink, self.get_notes()]

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
