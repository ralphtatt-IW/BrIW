import time


class Person:
    # name
    def __init__(self, first_name, surname, preference=None, team=None):
        self.name = first_name
        self.full_name = first_name + " " + surname
        self.surname = surname
        self.preference = preference
        self.team = team
        self.rounds_made = 0

    def __str__(self):
        return f"{self.full_name} ({self.team})"

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def made_round(self):
        self.rounds_made += 1

    def get_name(self):
        return self.full_name

    def get_preference(self):
        return self.preference

    def get_team(self):
        return self.team

    def get_rounds_made(self):
        return self.rounds_made

    def get_table_headers(self):
        return ["Name", "Team Name", "Fav. Drink", "Rounds Made"]

    def get_details(self):
        return [self.get_name(), self.get_team(), self.get_preference(), self.get_rounds_made()]

    def set_preference(self, preference):
        self.preference = preference


class Drink:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def get_table_headers(self):
        return ["Name"]

    def get_details(self):
        return [self.name]


class Team:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def get_table_headers(self):
        return ["Name", "Location"]

    def get_details(self):
        return [self.name, self.location]

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


# User makes an order for a drink
class Order:
    def __init__(self, person, drink, notes=None):
        self.person = person
        self.drink = drink
        self.notes = notes

    def change_order(self, new_drink):
        self.drink = new_drink

    def get_table_headers(self):
        return ["Person", "Drink", "Notes"]

    def get_notes(self):
        return self.notes

    def get_details(self):
        return [self.person, self.drink, self.get_notes()]

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


# A teams order is added to a round
class Round:
    def __init__(self, maker, team="General", length=600):
        self.maker = maker
        self.orders = []
        self.active = True
        self.team = team
        self.start_time = time.time()
        self.length = length

    def __str__(self):
        return f"Team:{self.team} - Maker:{self.maker.get_name()}"

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def get_maker(self):
        return self.maker

    def add_order(self, order):
        self.orders.append(order)

    def get_team(self):
        return self.team

    def elapsed_time(self):
        duration = time.time() - self.start_time
        if duration > 60:
            duration = duration / 60
            return str(round(duration)) + "m"
        return str(round(duration)) + "s"

    def finish_round(self):
        self.maker.rounds_made += 1
        self.duration = self.elapsed_time()
        self.active = False

    def get_order_size(self):
        return len(self.orders)

    def get_table_headers(self):
        if self.active:
            time_string = "Elasped Time"
        else:
            time_string = "Duration"
        return ["Team Name", "Maker", time_string, "Order Size"]

    def get_details(self):
        if self.active:
            time_type = self.elapsed_time()
        else:
            time_type = self.duration
        return [self.get_team(), self.get_maker(), time_type, self.get_order_size()]
