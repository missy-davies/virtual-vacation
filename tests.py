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
        self.assertIn(b'Share your best destination photos and inspire others', result.data)


    def test_gallery(self):
        """Test displaying gallery page"""

        result = self.client.get('/gallery')
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'Gallery', result.data)


    def test_add_images(self):
        """Test displaying add images page"""

        result = self.client.get('/add')
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'Add Images', result.data)


#------------------------------------------------------------------#

if __name__ == '__main__':
    import unittest

    os.system('dropdb testdb')
    os.system('createdb testdb')
    
    unittest.main(verbosity=2)