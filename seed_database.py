"""Script to seed database"""

import os
import sys 

import crud
import model
import server

os.system('dropdb virtualvacation')
os.system('createdb virtualvacation')

model.connect_to_db(server.app)
model.db.create_all()


# Add destinations 
italy = crud.create_destination('Italy')
france = crud.create_destination('France')
spain = crud.create_destination('Spain')

# Add starter images 
france_image_names = ['france1.jpeg', 'france2.jpeg', 'france3.jpeg', 
                'france4.jpeg', 'france5.jpeg']
                
spain_image_names = ['spain1.jpeg', 'spain2.jpeg', 'spain3.jpeg', 'spain4.jpeg', 
                     'spain5.jpeg', 'spain6.jpeg']
                    
italy_image_names = ['italy1.jpeg', 'italy2.jpeg', 'italy3.jpeg', 'italy4.jpeg',
                     'italy5.jpeg', 'italy6.jpeg', 'italy7.jpeg', 'italy8.jpeg']

for image in france_image_names:
    crud.create_image(image, france)

for image in spain_image_names:
    crud.create_image(image, spain)

for image in italy_image_names:
    crud.create_image(image, italy)