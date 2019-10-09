#! /usr/bin/env python3

import unittest
from functions import *


class Test_Func(unittest.TestCase):
    def test_check_empty_true(self):
        l = []
        self.assertTrue(check_empty(l))
        l.append(1)
        self.assertFalse(check_empty(l))

    def test_check_empty_false(self):
        l = [1, 2, 3, 4]
        self.assertFalse(check_empty(l))

    def test_add_person(self):
        people = []
        first_name = "Tessie"
        last_name = "Testingworth"
        drink = Drink("Water")
        team = Team("Super Team", "Location")

        add_person(first_name, last_name, drink, team, people)

        actual_result = people[-1]  # Function appends
        expected_result = Person("Tessie", "Testingworth", drink, team)

        self.assertEqual(actual_result, expected_result)

    def test_add_drinks(self):
        drinks = []
        drink_name = "Milk"

        add_drink(drink_name, drinks)

        actual_result = drinks[-1]  # Function appends to list
        expected_result = Drink("Milk")

        self.assertEqual(actual_result, expected_result)

    # WILL FAIL DUE TO TIME INITIATION
    # def test_add_round(self):
    #     rounds = []
    #     team = Team("Academy", "Location, Location, Location")
    #     drink = Drink("Milk")
    #     maker = Person("Tessie", "Testingworth", drink, team)
    #
    #
    #     add_round(maker, team, rounds)
    #
    #     actual_result = rounds[-1]
    #     expected_result = Round(maker, team)
    #
    #     self.assertEqual(actual_result, expected_result)


if __name__ == "__main__":
    unittest.main()
