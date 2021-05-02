"""Models for Virtual Vacation image repository app"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

import crud 

db = SQLAlchemy()


class Destination(db.Model):
    """A destination"""

    __tablename__ = 'destinations'

    destination_id = db.Column(db.Integer,
                                autoincrement=True,
                                primary_key=True)
    name = db.Column(db.String, unique=True)

    images = db.relationship('Image')

    def __repr__(self):
        return f'<Destination destination_id={self.destination_id} name={self.name}>'


class Image(db.Model):
    """An image"""

    __tablename__ = 'images'

    image_id = db.Column(db.Integer,
                         autoincrement=True,
                         primary_key=True)
    url = db.Column(db.String)
    destination_id = db.Column(db.Integer, db.ForeignKey('destinations.destination_id'))

    destination = db.relationship('Destination')

    def __repr__(self):
        return f'<Image image_id={self.image_id} url={self.url}>'


def connect_to_db(flask_app, db_uri='postgresql:///virtualvacation', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Yay, you successfully connected to the db!')


#------------------------------------------------------------------#

if __name__ == '__main__':
    from server import app

    connect_to_db(app)
