#! /usr/bin/env python3

from http.server import HTTPServer, BaseHTTPRequestHandler
import classes
import database_connect as dbc

drinks = dbc.get_all_drinks()
teams = dbc.get_all_teams()
people = dbc.get_all_people(drinks, teams)
rounds = dbc.get_all_rounds(people, teams)
orders = dbc.get_all_orders(drinks, people, rounds)

def render_drinks(drinks):
    drinks_html = ""
    for key in drinks:
        drinks_html += f'<li>{drinks[key]}</li>'
    return drinks_html

def render_people(people):
    people_html = ""
    for key in people:
        people_html += f'<li>{people[key]}</li>'
    return people_html

def render_rounds(rounds):
    rounds_html = ""
    for key in rounds:
        rounds_html += f'<li>{rounds[key]}</li>'
    return rounds_html

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Tell the client we're about to send HTML content in our HTTP payload
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()

        # Produce the HTML
        html_document = f"""
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" href="./css/master.css">
    </head>

    <body>
        <marquee>
        <p>Available drinks:</p>
        <ul>
            {render_drinks(drinks)}
        </ul>
        <p>Available People:</p>
        <ul>
            {render_people(people)}
        </ul>
        <p>Rounds:</p>
        <ul>
            {render_rounds(rounds)}
        </ul>
          <iframe id="myvideo" width="560" height="315" src="https://www.youtube.com/embed/HP362ccZBmY?autoplay=1&mute=0&controls=0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
         </marquee>
    </body>

</html>
"""
        # Render and send response
        self.wfile.write(html_document.encode('utf-8'))

if __name__ == "__main__":
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, Handler)
    print("Starting server")
    httpd.serve_forever()
