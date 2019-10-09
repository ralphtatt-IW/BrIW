#! /usr/bin/env python3
from flask import Flask, jsonify, request, render_template
import database_connect as dbc
from classes import *
from functions import *

app = Flask(__name__)


@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404


@app.route("/")
def home_page():
    return render_template('home.html', title="Home")


@app.route("/teams")
def teams_page():
    teams = dbc.get_all_teams()
    return render_template('teams.html', title="People", teams=teams)


@app.route('/add_team', methods=['GET', 'POST'])
def new_team():
    if request.method == "GET":
        return render_template('add_team.html', title="Add Team")

    if request.method == "POST":
        team_name = request.form.get("team-name")
        team_location = request.form.get("team-location")
        add_team(team_name, team_location)
        return teams_page()


@app.route('/view_team', methods=['GET', 'POST'])
def view_team():
    if request.method == "GET":
        return teams_page()

    if request.method == "POST":
        drinks = dbc.get_all_drinks()
        teams = dbc.get_all_teams()
        people = dbc.get_all_people(drinks, teams)

        result = request.form.to_dict()
        team_id = int(result["team_id"])
        team_name = teams[team_id].name

        return render_template('view_team.html',
                               team_id=team_id,
                               team_name=team_name,
                               people=people
                               )


@app.route('/add_member', methods=['GET', 'POST'])
def new_member():
    if request.method == "GET":
        drinks = dbc.get_all_drinks()
        teams = dbc.get_all_teams()
        return render_template('add_member.html', title="Add Member", drinks=drinks, teams=teams)

    if request.method == "POST":
        drinks = dbc.get_all_drinks()
        teams = dbc.get_all_teams()
        first_name = request.form.get("first_name")
        second_name = request.form.get("second_name")
        preference = drinks[int(request.form.get("drink_id"))]
        team = teams[int(request.form.get("team_id"))]
        add_person(first_name, second_name, preference, team)
        return teams_page()


@app.route("/drinks")
def drinks_page():
    drinks = dbc.get_all_drinks()
    return render_template('drinks.html', title="Drinks", drinks=drinks)


@app.route('/add_drink', methods=['GET', 'POST'])
def new_drink():
    if request.method == "GET":
        return render_template('add_drink.html', title="Add Drink")

    elif request.method == "POST":
        drink_name = request.form.get("drink-name")
        add_drink(drink_name)
        return drinks_page()


@app.route("/rounds")
def rounds_page():
    drinks = dbc.get_all_drinks()
    teams = dbc.get_all_teams()
    people = dbc.get_all_people(drinks, teams)
    rounds = dbc.get_all_rounds(people, teams)
    orders = dbc.get_all_orders(drinks, people, rounds)
    return render_template('rounds.html', title="Rounds", rounds=rounds)


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
        pretty_orders.append(
            [o.order_id, o.round_id, o.drink.__str__(), o.person.__str__(), o.notes])

    return render_template('view_orders.html', title="Do I even need a title", orders=pretty_orders)


######################### API ##########################
@app.route("/api/people", methods=['GET'])
def get_person():
    drinks = dbc.get_all_drinks()
    teams = dbc.get_all_teams()
    people = dbc.get_all_people(drinks, teams)
    return jsonify([person.to_json() for person in list(people.values())])


@app.route("/api/rounds", methods=['GET'])
def get_rounds():
    drinks = dbc.get_all_drinks()
    teams = dbc.get_all_teams()
    people = dbc.get_all_people(drinks, teams)
    rounds = dbc.get_all_rounds(people, teams)
    orders = dbc.get_all_orders(drinks, people, rounds)
    return jsonify([round.to_json() for round in list(rounds.values())])


@app.route("/api/drinks", methods=['GET'])
def get_drinks():
    if request.method == "GET":
        drinks = dbc.get_all_drinks()
        return jsonify([drink.to_json() for drink in list(drinks.values())])


@app.route("/api/teams", methods=['GET'])
def get_teams():
    teams = dbc.get_all_teams()
    return jsonify([team.to_json() for team in list(teams.values())])


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=42069)
