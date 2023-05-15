from flask import Flask, request, render_template
import sqlite3 as sl

app = Flask(__name__)

@app.route("/")
def lookup():
    # TODO: open/create Vehicles.db sqlite3 database

    # TODO: create Vehicles table

    # TODO: bulk import some Vehicles

    # TODO: Search for vehicle by manufacturer_name parameter

    # TODO: render the vehicle_lookup.html template
    return

app.run()