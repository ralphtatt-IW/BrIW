#! /usr/bin/env python3
import database_connect as dbc
from encoder import *
from classes import *

from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class Drink_Handler(BaseHTTPRequestHandler):
    def _set_header(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/json')
        self.end_headers()

    def do_GET(self):
        self._set_header()

        drinks = dbc.get_all_drinks()

        jd = json.dumps(drinks, cls=MyEncoder)

        self.wfile.write(jd.encode('utf-8'))

    def do_POST(self):

        content_length = int(self.headers['Content-Length'])
        data = json.loads(self.rfile.read(content_length))

        drink = Drink(data["name"])

        dbc.save_drink(drink)

        self.send_response(201)
        self.end_headers()

if __name__ == "__main__":
    server_address = ('0.0.0.0', 8080)
    httpd = HTTPServer(server_address, Drink_Handler)
    print("Starting server...")

    httpd.serve_forever()
