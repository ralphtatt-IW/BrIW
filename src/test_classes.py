#! /usr/bin/env python3

import unittest
from classes import *


class Test_Drink(unittest.TestCase):
    def test_to_string(self):
        drink = Drink(1, "Milk")

        expected_result = "Milk"

        actual_result = str(drink)

        self.assertEqual(actual_result, expected_result)

    def test_get_table_header(self):
        drink = Drink(1, "Milk")

        expected_result = ["Name"]

        actual_result = drink.get_table_headers()

        self.assertEqual(actual_result, expected_result)

    def test_get_details(self):
        drink = Drink(1, "Milk")

        expected_result = ["Milk"]

        actual_result = drink.get_details()

        self.assertEqual(actual_result, expected_result)

    def test_equal_to_true(self):
        first_drink = Drink(1, "Milk")

        second_drink = Drink(1, "Milk")

        self.assertEqual(first_drink, second_drink)

    def test_equal_to_false(self):
        first_drink = Drink(1, "Milk")

        second_drink = Drink(1, "Not Milk")

        self.assertNotEqual(first_drink, second_drink)


class Test_Team(unittest.TestCase):
    def test_get_table_headers(self):
        team = Team(1, "Academy", "2nd Floor")

        actual_result = team.get_table_headers()

        expected_result = ["Name", "Location"]

        self.assertEqual(actual_result, expected_result)

    def test_get_details(self):
        team = Team(1, "Academy", "2nd Floor")

        actual_result = team.get_details()

        expected_result = ["Academy", "2nd Floor"]

        self.assertEqual(actual_result, expected_result)

    def test_to_string(self):
        team = Team(1, "Academy", "2nd Floor")

        expected_result = "Academy"

        actual_result = str(team)

        self.assertEqual(actual_result, expected_result)


class Test_Person(unittest.TestCase):
    #
    # def get_sql_values(self):
    #     drink = Drink(1,"Milk")
    #     team = Team(1,"Academy", "2nd Floor")
    #     person = Person(1,"Tessie", "Testingworth", drink, team)
    #
    #     actual_result = person.add_this_person_to_database();
    #     expected_result = "VALUES('Tessie','Testingworth','{team.get_}')"
    #     pass

    def test_to_string(self):
        drink = Drink(1, "Milk")
        team = Team(1, "Academy", "2nd Floor")
        person = Person(1, "Tessie", "Testingworth", team, drink)

        actual_result = str(person)
        expected_result = "Tessie Testingworth (Academy)"

        self.assertEqual(actual_result, expected_result)

    def test_get_name(self):
        drink = Drink(1, "Milk")
        team = Team(1, "Academy", "2nd Floor")
        person = Person(1, "Tessie", "Testingworth", team, drink)

        actual_result = person.get_name()
        expected_result = "Tessie Testingworth"

        self.assertEqual(actual_result, expected_result)

    def test_get_preference(self):
        drink = Drink(1, "Milk")
        team = Team(1, "Academy", "2nd Floor")
        person = Person(1, "Tessie", "Testingworth", team, drink)

        actual_result = person.get_preference()
        expected_result = drink

        print(actual_result)
        print(expected_result)

        self.assertEqual(actual_result, expected_result)

    def test_get_team(self):
        drink = Drink(1, "Milk")
        team = Team(1, "Academy", "2nd Floor")
        person = Person(1, "Tessie", "Testingworth", team, drink)

        actual_result = person.get_team()
        expected_result = team

        self.assertEqual(actual_result, expected_result)

    def test_get_table_headers(self):
        drink = Drink(1, "Milk")
        team = Team(1, "Academy", "2nd Floor")
        person = Person(1, "Tessie", "Testingworth", team, drink)

        actual_result = person.get_table_headers()
        expected_result = ["Name", "Team Name", "Fav. Drink"]

        self.assertEqual(actual_result, expected_result)

    def test_get_details(self):
        drink = Drink(1, "Milk")
        team = Team(1, "Academy", "2nd Floor")
        person = Person(1, "Tessie", "Testingworth", team, drink)

        actual_result = person.get_details()
        expected_result = [
            person.get_name(),
            person.get_team(),
            person.get_preference(),
        ]

        self.assertEqual(actual_result, expected_result)

    def test_set_preference(self):
        drink = Drink(1, "Milk")
        team = Team(1, "Academy", "2nd Floor")
        person = Person(1, "Tessie", "Testingworth", team, drink)
        new_drink = Drink(1, "Coffee")

        person.set_preference(new_drink)

        actual_result = person.get_preference()
        expected_result = new_drink

        self.assertEqual(actual_result, expected_result)


class Test_Order(unittest.TestCase):
    def test_get_table_headers(self):
        drink = Drink(1, "Milk")
        team = Team(1, "Academy", "2nd Floor")
        person = Person(1, "Tessie", "Testingworth", team, drink)
        order = Order(1, drink, person, 1, "")

        expected_result = ["Person", "Drink", "Notes"]
        actual_result = order.get_table_headers()

        self.assertEqual(actual_result, expected_result)

    def test_get_notes(self):
        drink = Drink(1, "Milk")
        team = Team(1, "Academy", "2nd Floor")
        person = Person(1, "Tessie", "Testingworth", team, drink)
        order = Order(1, drink, person, 1, "Extra Milk")

        expected_result = "Extra Milk"
        actual_result = order.get_notes()

        self.assertEqual(actual_result, expected_result)

    def test_get_details(self):
        drink = Drink(1, "Milk")
        team = Team(1, "Academy", "2nd Floor")
        person = Person(1, "Tessie", "Testingworth", team, drink)
        order = Order(1, drink, person, 1, "Extra Milk")

        expected_result = [person, drink, "Extra Milk"]
        actual_result = order.get_details()

        self.assertEqual(actual_result, expected_result)


class Test_Round(unittest.TestCase):

    def test_to_string(self):
        drink = Drink(1, "Milk")
        team = Team(1, "Academy", "2nd Floor")
        person = Person(1, "Tessie", "Testingworth", team, drink)
        round = Round(1, person, 1, team)

        expected_result = "Team:Academy - Maker:Tessie Testingworth"
        actual_result = str(round)

        self.assertEqual(actual_result, expected_result)

    def test_get_maker(self):
        drink = Drink(1, "Milk")
        team = Team(1, "Academy", "2nd Floor")
        person = Person(1, "Tessie", "Testingworth", team, drink)
        round = Round(1, person, 1, team)

        expected_result = person
        actual_result = round.get_maker()

        self.assertEqual(actual_result, expected_result)

    def test_get_team(self):
        drink = Drink(1, "Milk")
        team = Team(1, "Academy", "2nd Floor")
        person = Person(1, "Tessie", "Testingworth", team, drink)
        round = Round(1, person, 1, team)

        expected_result = team
        actual_result = round.get_team()

        self.assertEqual(actual_result, expected_result)

    def test_add_order(self):
        drink = Drink(1, "Milk")
        team = Team(1, "Academy", "2nd Floor")
        person = Person(1, "Tessie", "Testingworth", team, drink)
        round = Round(1, person, 1, team)
        order = Order(1, drink, person, 1, "Extra Milk")
        round.add_order(order)

        expected_result = {order.order_id : order}
        actual_result = round.orders

        self.assertEqual(actual_result, expected_result)

    def test_get_order_size(self):
        drink = Drink(1, "Milk")
        team = Team(1, "Academy", "2nd Floor")
        person = Person(1, "Tessie", "Testingworth", team, drink)
        round = Round(1, person, 1, team)
        order = Order(1, drink, person, 1, "Extra Milk")
        round.add_order(order)

        expected_result = 1
        actual_result = round.get_order_size()

        self.assertEqual(actual_result, expected_result)

    def test_get_table_headers_active(self):
        drink = Drink(1, "Milk")
        team = Team(1, "Academy", "2nd Floor")
        person = Person(1, "Tessie", "Testingworth", team, drink)
        round = Round(1, person, 1, team)

        expected_result = ["Team Name", "Maker", "Active"]
        actual_result = round.get_table_headers()

        self.assertEqual(actual_result, expected_result)

    # def test_get_details(self):
    #     if self.active:
    #         time_type = self.elapsed_time()
    #     else:
    #         time_type = self.duration
    #     return [self.get_team(), self.get_maker(), time_type, self.get_order_size()]
    # def elapsed_time(self):
    #     duration = time.time() - self.start_time
    #     if duration > 60:
    #         duration = duration / 60
    #         return str(round(duration)) + "m"
    #     return str(round(duration)) + "s"


if __name__ == "__main__":
    unittest.main()
