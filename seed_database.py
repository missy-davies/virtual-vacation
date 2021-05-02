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
destination_names = ['Italy', 'France', 'Spain']
for name in destination_names:
    crud.create_destination(name)

# Add starter images 