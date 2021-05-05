"""Script to test Flask routes and server"""

from unittest import TestCase
from server import app

import os 


class FlaskTestBasic(TestCase):
    """Flask server tests"""

    def setUp(self):
        """Stuff to do before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True
    
    
    def tearDown(self):
        """Stuff to do after every test"""

        self.client = None
        app.config['TESTING'] = False


    def test_homepage(self):
        """Test displaying homepage"""

        result = self.client.get('/')
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'Browse photo collections by destination and get inspiration for your next trip', result.data)


    def test_destination(self):
        """Test displaying destinations page"""

        result = self.client.get('/destination')
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'ADD SOMETHING HERE', result.data)
        # TODO: Add text to check above 

    def test_upload_images(self):
        """Test displaying upload images page"""

        result = self.client.get('/upload')
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'Upload Images', result.data)
        # TODO: To update

#------------------------------------------------------------------#

if __name__ == '__main__':
    import unittest

    os.system('dropdb testdb')
    os.system('createdb testdb')
    
    unittest.main(verbosity=2)