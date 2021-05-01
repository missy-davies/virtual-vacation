"""Models for Virtual Vacation image repository app"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()




def connect_to_db(flask_app, db_uri='postgresql:///virtualvacation', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Yay, you successfully connected to the db!')


if __name__ == '__main__':
    from server import app

    connect_to_db(app)
