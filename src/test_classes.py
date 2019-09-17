#! /usr/bin/env python3

import unittest
from main import *


class Test_Drink(unittest.TestCase):
    def test_to_string(self):
        drink = Drink("Milk")

        expected_result = "Milk"

        actual_result = str(drink)

        self.assertEqual(actual_result, expected_result)

    def test_get_table_header(self):
        drink = Drink("Milk")

        expected_result = ["Name"]

        actual_result = drink.get_table_headers()

        self.assertEqual(actual_result, expected_result)

    def test_get_details(self):
        drink = Drink("Milk")

        expected_result = ["Milk"]

        actual_result = drink.get_details()

        self.assertEqual(actual_result, expected_result)


class Test_Team(unittest.TestCase):
    def test_get_table_headers(self):
        team = Team("Academy", "2nd Floor")

        actual_result = team.get_table_headers()

        expected_result = ["Name", "Location"]

        self.assertEqual(actual_result, expected_result)

    def test_get_details(self):
        team = Team("Academy", "2nd Floor")

        actual_result = team.get_details()

        expected_result = ["Academy", "2nd Floor"]

        self.assertEqual(actual_result, expected_result)

    def test_to_string(self):
        team = Team("Academy", "2nd Floor")

        expected_result = "Academy"

        actual_result = str(team)

        self.assertEqual(actual_result, expected_result)


class Test_Person(unittest.TestCase):

    def test_to_string(self):
        drink = Drink("Milk")
        team = Team("Academy", "2nd Floor")
        person = Person("Tessie", "Testingworth", drink, team)

        actual_result = str(person)
        expected_result = "Tessie Testingworth (Academy)"

        self.assertEqual(actual_result, expected_result)

    def test_get_rounds_made(self):
        drink = Drink("Milk")
        team = Team("Academy", "2nd Floor")
        person = Person("Tessie", "Testingworth", drink, team)

        actual_result = person.get_rounds_made()
        expected_result = 0

        self.assertEqual(actual_result, expected_result)

    def test_made_round(self):
        drink = Drink("Milk")
        team = Team("Academy", "2nd Floor")
        person = Person("Tessie", "Testingworth", drink, team)

        person.made_round()

        actual_result = person.get_rounds_made()
        expected_result = 1

        self.assertEqual(actual_result, expected_result)

    def test_get_name(self):
        drink = Drink("Milk")
        team = Team("Academy", "2nd Floor")
        person = Person("Tessie", "Testingworth", drink, team)

        actual_result = person.get_name()
        expected_result = "Tessie Testingworth"

        self.assertEqual(actual_result, expected_result)

    def test_get_preference(self):
        drink = Drink("Milk")
        team = Team("Academy", "2nd Floor")
        person = Person("Tessie", "Testingworth", drink, team)

        actual_result = person.get_preference()
        expected_result = drink

        self.assertEqual(actual_result, expected_result)

    def test_get_team(self):
        drink = Drink("Milk")
        team = Team("Academy", "2nd Floor")
        person = Person("Tessie", "Testingworth", drink, team)

        actual_result = person.get_team()
        expected_result = team

        self.assertEqual(actual_result, expected_result)

    def test_get_table_headers(self):
        drink = Drink("Milk")
        team = Team("Academy", "2nd Floor")
        person = Person("Tessie", "Testingworth", drink, team)

        actual_result = person.get_table_headers()
        expected_result = ["Name", "Team Name", "Fav. Drink", "Rounds Made"]

        self.assertEqual(actual_result, expected_result)

    def test_get_details(self):
        drink = Drink("Milk")
        team = Team("Academy", "2nd Floor")
        person = Person("Tessie", "Testingworth", drink, team)

        actual_result = person.get_details()
        expected_result = [person.get_name(), person.get_team(), person.get_preference(), person.get_rounds_made()]

        self.assertEqual(actual_result, expected_result)

    def test_set_preference(self):
        drink = Drink("Milk")
        team = Team("Academy", "2nd Floor")
        person = Person("Tessie", "Testingworth", drink, team)
        new_drink = Drink("Coffee")

        person.set_preference(new_drink)

        actual_result = person.get_preference()
        expected_result = new_drink

        self.assertEqual(actual_result, expected_result)


class Test_Order(unittest.TestCase):
    def test_change_order(self):
        drink = Drink("Milk")
        team = Team("Academy", "2nd Floor")
        person = Person("Tessie", "Testingworth", drink, team)
        order = Order(person, drink)

        new_drink = Drink("Water")

        order.change_order(new_drink)

        expected_result = new_drink
        actual_result = order.drink

        self.assertEqual(actual_result, expected_result)


    def test_get_table_headers(self):
        drink = Drink("Milk")
        team = Team("Academy", "2nd Floor")
        person = Person("Tessie", "Testingworth", drink, team)
        order = Order(person, drink)

        expected_result = ["Person", "Drink", "Notes"]
        actual_result = order.get_table_headers()

        self.assertEqual(actual_result, expected_result)

    def test_get_notes(self):
        drink = Drink("Milk")
        team = Team("Academy", "2nd Floor")
        person = Person("Tessie", "Testingworth", drink, team)
        order = Order(person, drink, "Extra Milk")

        expected_result = "Extra Milk"
        actual_result = order.get_notes()

        self.assertEqual(actual_result, expected_result)

    def test_get_details(self):
        drink = Drink("Milk")
        team = Team("Academy", "2nd Floor")
        person = Person("Tessie", "Testingworth", drink, team)
        order = Order(person, drink, "Extra Milk")

        expected_result = [person, drink, "Extra Milk"]
        actual_result = order.get_details()

        self.assertEqual(actual_result, expected_result)


class Test_Round(unittest.TestCase):

    def test_to_string(self):
        drink = Drink("Milk")
        team = Team("Academy", "2nd Floor")
        person = Person("Tessie", "Testingworth", drink, team)
        round = Round(person, team)

        expected_result = "Team:Academy - Maker:Tessie Testingworth"
        actual_result = str(round)

        self.assertEqual(actual_result, expected_result)

    def test_get_maker(self):
        drink = Drink("Milk")
        team = Team("Academy", "2nd Floor")
        person = Person("Tessie", "Testingworth", drink, team)
        round = Round(person, team)

        expected_result = person
        actual_result = round.get_maker()

        self.assertEqual(actual_result, expected_result)

    def test_get_team(self):
        drink = Drink("Milk")
        team = Team("Academy", "2nd Floor")
        person = Person("Tessie", "Testingworth", drink, team)
        round = Round(person, team)

        expected_result = team
        actual_result = round.get_team()

        self.assertEqual(actual_result, expected_result)

    def test_finish_round_active(self):
        drink = Drink("Milk")
        team = Team("Academy", "2nd Floor")
        person = Person("Tessie", "Testingworth", drink, team)
        round = Round(person, team)

        round.finish_round()

        expected_result = False
        actual_result = round.active

        self.assertEqual(actual_result, expected_result)

    def test_finish_round_person_made(self):
        drink = Drink("Milk")
        team = Team("Academy", "2nd Floor")
        person = Person("Tessie", "Testingworth", drink, team)
        round = Round(person, team)

        round.finish_round()

        expected_result = 1
        actual_result = person.rounds_made

        self.assertEqual(actual_result, expected_result)

    def test_add_order(self):
        drink = Drink("Milk")
        team = Team("Academy", "2nd Floor")
        person = Person("Tessie", "Testingworth", drink, team)
        round = Round(person, team)
        order = Order(person, drink, "Extra Milk")
        round.add_order(order)

        expected_result = [order]
        actual_result = round.orders

        self.assertEqual(actual_result, expected_result)

    def test_get_order_size(self):
        drink = Drink("Milk")
        team = Team("Academy", "2nd Floor")
        person = Person("Tessie", "Testingworth", drink, team)
        round = Round(person, team)
        order = Order(person, drink, "Extra Milk")
        round.add_order(order)

        expected_result = 1
        actual_result = round.get_order_size()

        self.assertEqual(actual_result, expected_result)

    def test_get_table_headers_active(self):
        drink = Drink("Milk")
        team = Team("Academy", "2nd Floor")
        person = Person("Tessie", "Testingworth", drink, team)
        round = Round(person, team)

        expected_result =  ["Team Name", "Maker", "Elasped Time", "Order Size"]
        actual_result = round.get_table_headers()

        self.assertEqual(actual_result, expected_result)

    def test_get_table_headers_inactive(self):
        drink = Drink("Milk")
        team = Team("Academy", "2nd Floor")
        person = Person("Tessie", "Testingworth", drink, team)
        round = Round(person, team)
        round.finish_round()

        expected_result =  ["Team Name", "Maker", "Duration", "Order Size"]
        actual_result = round.get_table_headers()

        self.assertEqual(actual_result, expected_result)

    # def elapsed_time(self):
    #     duration = time.time() - self.start_time
    #     if duration > 60:
    #         duration = duration / 60
    #         return str(round(duration)) + "m"
    #     return str(round(duration)) + "s"
    #
    # def get_order_size(self):
    #     return len(self.orders)
    #

    # def test_get_details(self):
    #     if self.active:
    #         time_type = self.elapsed_time()
    #     else:
    #         time_type = self.duration
    #     return [self.get_team(), self.get_maker(), time_type, self.get_order_size()]

    # def add_order(self, order):
    #     self.orders.append(order)

# class Test_Func(unittest.TestCase):
#     def test_add_person(self):
#         people = []
#         f_name = "Tessie"
#         l_name = "Testington"
#         pref = Drink("Coffee")
#         team = Team("Academy", "2nd Floor")
#
#         add_person(f_name, l_name, pref, team)

if __name__ == "__main__":
    unittest.main()
