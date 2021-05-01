"""Server for Virtual Vacation image repository"""

from flask import Flask, render_template, request, flash, redirect
import jinja2

import os
import sys 

from model import connect_to_db

app = Flask(__name__)
app.secret_key = "demosecretkey"


@app.route('/')
def show_homepage():
    """Display homepage"""

    return render_template('home.html')


@app.route('/gallery')
def show_gallery():
    """Display image gallery"""

    return render_template('gallery.html')


@app.route('/add')
def add_images():
    """Display page for visitors to upload images"""

    return render_template('add.html')



#------------------------------------------------------------------#

if __name__ == "__main__":
    connect_to_db(app)
    app.run(debug=True, host="0.0.0.0")