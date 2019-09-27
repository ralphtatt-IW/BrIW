import pymysql
import os
from classes import *
import subprocess


def get_details_from_keychain(name):
    pipe = subprocess.Popen(["security", "find-generic-password", "-s", name, "-w"],
                            stdout=subprocess.PIPE, text=True)
    out, err = pipe.communicate()
    return None if err else out.strip(" \n")


def make_connection():
    try:
        connection = pymysql.connect(
            get_details_from_keychain("BRIW_DB_HOST"),  # host
            get_details_from_keychain("BRIW_DB_USER"),  # username
            get_details_from_keychain("BRIW_DB_PASS"),  # password
            get_details_from_keychain("BRIW_DB_DB")  # database
        )
        return connection
    except:
        print("Can't connect to database!")
        exit()


def close_connection(connection):
    connection.close()


def get_max_id_from_table(table_name, column_name):
    try:
        con = make_connection()
        with con.cursor() as cursor:

            # Execute Query
            cursor.execute(f"SELECT MAX({column_name}) FROM {table_name}")

            results = cursor.fetchall()

            max_value = results[0][0]

    finally:
        close_connection(con)

    return max_value


def get_fresh_id(table_name, column_name):
    return get_max_id_from_table(table_name, column_name) + 1


def save_drink(drink):
    try:
        con = make_connection()
        with con.cursor() as cursor:
            cursor.execute(f"INSERT INTO Drinks(drink_id, name) VALUES({drink.drink_id}, '{drink.name}')")
            con.commit()
    finally:
        close_connection(con)


def get_all_drinks():
    drinks = {}
    try:
        con = make_connection()
        with con.cursor() as cursor:

            # Execute Query
            cursor.execute("SELECT * FROM Drinks")

            drinks_data = cursor.fetchall()
            # Turn returned data into dict of
            for d in drinks_data:
                drinks[d[0]] = Drink(d[0], d[1])

    finally:
        close_connection(con)

    return drinks


def save_team(team):
    try:
        con = make_connection()
        with con.cursor() as cursor:
            cursor.execute(f"""INSERT INTO Teams(team_id, name, location)
                            VALUES({team.team_id}, '{team.name}', '{team.location}')""")
            con.commit()
    finally:
        close_connection(con)


def get_all_teams():
    teams = {}
    try:
        con = make_connection()
        with con.cursor() as cursor:

            # Execute Query
            cursor.execute("SELECT * FROM Teams")

            t_data = cursor.fetchall()
            # Turn returned data into dict of
            for t in t_data:
                teams[t[0]] = Team(t[0], t[1], t[2])

    finally:
        close_connection(con)

    return teams


def save_person(person):
    try:
        con = make_connection()
        with con.cursor() as cursor:
            cursor.execute(f"""INSERT INTO People(person_id, first_name, second_name, team, drink_pref)
                               VALUES({person.person_id}, '{person.first_name}', '{person.second_name}',
                               {person.team.team_id}, {person.preference.drink_id})""")
            con.commit()
    finally:
        close_connection(con)


def get_all_people(drinks, teams):
    people = {}
    try:
        con = make_connection()
        with con.cursor() as cursor:

            # Execute Query
            cursor.execute("SELECT * FROM People")

            p_data = cursor.fetchall()
            # Turn returned data into dict of
            for p in p_data:
                people[p[0]] = Person(p[0], p[1], p[2], teams[p[3]], drinks[p[4]])

    finally:
        close_connection(con)

    return people


def save_round(round):
    try:
        con = make_connection()
        with con.cursor() as cursor:
            cursor.execute(f"""INSERT INTO Rounds(round_id, maker_id, active, team_id)
                               VALUES({round.round_id}, {round.maker.person_id}, {round.active},
                               {round.team.team_id})""")
            con.commit()
    finally:
        close_connection(con)


def get_all_rounds(people, teams):
    rounds = {}
    try:
        con = make_connection()
        with con.cursor() as cursor:
            cursor.execute("SELECT * FROM Rounds")

            r_data = cursor.fetchall()

            for r in r_data:
                rounds[r[0]] = Round(r[0], people[r[1]], r[2], teams[r[3]])

    finally:
        close_connection(con)

    return rounds


def save_order(order):
    try:
        con = make_connection()
        with con.cursor() as cursor:
            cursor.execute(f"""INSERT INTO Orders(order_id, drink_id, person_id, round_id, notes)
                               VALUES({order.order_id}, {order.drink_id}, {order.person_id},
                               {order.round_id}, '{order.notes}')""")
            con.commit()
    finally:
        close_connection(con)


def get_all_orders(drinks, people, rounds):
    orders = {}
    try:
        con = make_connection()
        with con.cursor() as cursor:
            cursor.execute("SELECT * FROM Orders")

            o_data = cursor.fetchall()

            for o in o_data:
                orders[o[0]] = Order(o[0], drinks[o[1]], people[o[2]], o[3], o[4])
                rounds[o[3]].add_order(orders[o[0]])

    finally:
        close_connection(con)

    return orders
