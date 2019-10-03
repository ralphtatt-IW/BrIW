#! /usr/bin/env python3
from flask import Flask, jsonify, request, render_template
import database_connect as dbc
from classes import *
from functions import *

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Absolutely dank"


@app.route("/drinks", methods=['GET'])
def get_drinks():
    if request.method == "GET":
        drinks = dbc.get_all_drinks()
        return jsonify([drink.to_json() for drink in list(drinks.values())])


@app.route('/new_drink', methods=['GET', 'POST'])
def new_drink():
    if request.method == "GET":
        return render_template('drinks_form.html', title="Create form")

    elif request.method == "POST":
        drink_name = request.form.get("drink-name")
        add_drink(drink_name)
        return render_template("return_drink.html", title="Posted", drink=drink_name)


@app.route("/teams", methods=['GET'])
def get_teams():
    teams = dbc.get_all_teams()
    return jsonify([team.to_json() for team in list(teams.values())])

@app.route('/new_team', methods=['GET', 'POST'])
def new_team():
    if request.method == "GET":
        return render_template('teams_form.html', title="Create form")

    elif request.method == "POST":
        team_name = request.form.get("team-name")
        team_location = request.form.get("team-location")
        add_team(team_name, team_location)
        return render_template("return_team.html", title="Posted", name=team_name, location=team_location)


@app.route("/people", methods=['GET'])
def get_person():
    drinks = dbc.get_all_drinks()
    teams = dbc.get_all_teams()
    people = dbc.get_all_people(drinks, teams)
    return jsonify([person.to_json() for person in list(people.values())])


@app.route("/rounds", methods=['GET'])
def get_rounds():
    drinks = dbc.get_all_drinks()
    teams = dbc.get_all_teams()
    people = dbc.get_all_people(drinks, teams)
    rounds = dbc.get_all_rounds(people, teams)
    orders = dbc.get_all_orders(drinks, people, rounds)
    return jsonify([round.to_json() for round in list(rounds.values())])

@app.route('/new_order', methods=['GET', 'POST'])
def new_order():
    if request.method == "GET":
        drinks = dbc.get_all_drinks()
        teams = dbc.get_all_teams()
        people = dbc.get_all_people(drinks, teams)
        rounds = dbc.get_all_rounds(people, teams)
        return render_template('new_order.html', title="Create form", people=people, rounds=rounds)

    elif request.method == "POST":
        drinks = dbc.get_all_drinks()
        teams = dbc.get_all_teams()
        people = dbc.get_all_people(drinks, teams)
        rounds = dbc.get_all_rounds(people, teams)

        round_key = request.form.get("round-name")
        person_key = request.form.get("person-name")
        notes = request.form.get("notes")
        person = people[int(person_key)]
        add_order(person, person.preference, rounds[int(round_key)], notes)
        return render_template("return_order.html", title="Posted")

@app.route('/view_orders', methods=['GET'])
def view_orders():
        drinks = dbc.get_all_drinks()
        teams = dbc.get_all_teams()
        people = dbc.get_all_people(drinks, teams)
        rounds = dbc.get_all_rounds(people, teams)
        orders = dbc.get_all_orders(drinks, people, rounds)
        pretty_orders = []
        for o in list(orders.values()):
            pretty_orders.append([o.order_id, o.round_id, o.drink.__str__(), o.person.__str__(), o.notes])

        return render_template('view_orders.html', title="Do I even need a title", orders=pretty_orders)

if __name__ == "__main__":
    app.run(host='localhost', port=42069)
