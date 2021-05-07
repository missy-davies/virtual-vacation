"""Script to test Flask routes and server"""

from unittest import TestCase
from server import app
import crud 
from model import Destination, Image, connect_to_db, db
# from selenium import webdriver 

import os 

def example_data():
    """Create example data for testing"""

    italy = crud.create_destination('Italy')

    img1 = crud.create_image('italy1.jpeg', italy)
    img2 = crud.create_image('italy2.jpeg', italy)


class FlaskTests(TestCase):
    def setUp(self):
        """Stuff to do before every test."""

        # Get the Flask test client
        self.client = app.test_client()

        # Show Flask errors that happen during tests
        app.config['TESTING'] = True

        # Connect to test database
        connect_to_db(app, "postgresql:///testdb")

        # Create tables and add sample data
        db.create_all()
        example_data()


    def tearDown(self):
        """Do at end of every test."""

        db.session.close()
        db.drop_all()


    def test_get_destination(self):
        """Can we get a Destination out of the sample data?"""

        italy = Destination.query.filter(Destination.name == "Italy").first()
        self.assertEqual(italy.name, "Italy")


    def test_get_image(self):
        """Can we get an image out of the sample data?"""

        img1 = Image.query.filter(Image.url == "italy1.jpeg").first()
        self.assertEqual(img1.url, "italy1.jpeg")


    def test_homepage(self):
        """Test displaying homepage"""

        result = self.client.get('/')
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'Browse photo collections by destination and get inspiration', result.data)
   
   
    def test_display_destination(self):
        """Test displaying individual destination page, in this example for Italy"""

        result = self.client.get(f"/destinations/1")

        self.assertIn(b'Italy', result.data)
    
    
    def test_display_image(self):
        """Test displaying individual image page, in this example for img1"""

        result = self.client.get(f"/image/1")

        self.assertIn(b'<img class="fill img-thumbnail" src="/static/img/uploads/italy1.jpeg">', result.data)
    
    
    def test_display_upload(self):
        """Test displaying upload images"""

        result = self.client.get(f"/upload")

        self.assertIn(b'Upload an image', result.data)


#------------------------------------------------------------------#

if __name__ == '__main__':
    import unittest

    os.system('dropdb testdb')
    os.system('createdb testdb')
    
    unittest.main(verbosity=2)