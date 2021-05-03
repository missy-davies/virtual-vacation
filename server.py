"""Server for Virtual Vacation image repository"""

from flask import Flask, render_template, request, flash, redirect
import jinja2

from model import db, connect_to_db, Image, Destination
import crud 

import os
import sys 

app = Flask(__name__)
app.secret_key = "demosecretkey"


@app.route('/')
def show_homepage():
    """Display homepage"""

    destinations = crud.return_destinations()
    
    return render_template('home.html', destinations=destinations)


@app.route('/destination/<destination_id>')
def show_gallery(destination_id):
    """Display page for each destination with images"""

    # TODO: Need to write this crud function 
    destination = crud.get_destination_by_id(destination_id)
    destination_images = crud.get_images_by_destination(destination)

    return render_template('destination-details.html', destination=destination,
                                                       destination_images=destination_images)


@app.route('/add')
def add_images():
    """Display page for visitors to upload images"""

    destinations = crud.return_destinations()

    return render_template('add.html', destinations=destinations)



#------------------------------------------------------------------#

if __name__ == "__main__":
    connect_to_db(app)
    app.run(debug=True, host="0.0.0.0")