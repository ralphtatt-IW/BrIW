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
            get_details_from_keychain("BRIW_DB_HOST"), #host
            get_details_from_keychain("BRIW_DB_USER"), #username
            get_details_from_keychain("BRIW_DB_PASS"), #password
            get_details_from_keychain("BRIW_DB_DB") # database
        )
        return connection
    except:
        print("Can't connect to database!")
        exit()

def close_connection(connection):
    connection.close()

def save_drink(drink):
    try:
        con = make_connection()
        with con.cursor() as cursor:
            cursor.execute(f"INSERT INTO Drinks(name) VALUES('{drink.name}')")
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
            for drink in drinks_data:
                drinks[drink[0]] = Drink(drink[1]);

    finally:
        close_connection(con)

    return drinks

def save_team(team):
    try:
        con = make_connection()
        with con.cursor() as cursor:
            cursor.execute(f"INSERT INTO Teams(name, location) VALUES('{team.name}', '{team.location}')")
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
                teams[t[0]] = Team(t[1], t[2]);

    finally:
        close_connection(con)

    return teams

def get_all_people():
    people = {}
    try:
        con = make_connection()
        with con.cursor() as cursor:

            # Execute Query
            cursor.execute("SELECT * FROM People")

            p_data = cursor.fetchall()
            # Turn returned data into dict of
            for p in p_data:
                people[p[0]] = People(t[1], t[2]);

    finally:
        close_connection(con)

    return teams
