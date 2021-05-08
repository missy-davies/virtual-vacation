# Virtual Vacation 
## Overview
Virtual Vacation is a community web app to share photos and inspire others
for their next trip! Visitors can browse images by destination or upload
their own images to a collection to inspire others. 

Virtual Vacation is built with Python Flask on the backend with a PostgreSQL database,
and Javascript/jQuery on the frontend along with HTML/CSS and Bootstrap. 

Please see ![this video for a full walkthrough](LINK HERE). 

## Features 
#### Browse Images by Destination  
Visitors can browse images by selectd destination.
![Browse Images](/static/img/features/browse.gif)

#### Upload Images 
Visitors can upload images to any collection. 
![Upload Images](/static/img/features/upload.gif)

## Technologies
Languages:
- Python 3
- JavaScript
- HTML
- CSS

Frameworks & Libraries:
- Flask
- Jinja
- Bootstrap 

Database:
 - PostgreSQL / SQLAlchemy

## Getting Started  
To download and use Virtual Vacation please follow these instructions:
1. In your terminal, `git clone` this repository 
2. Navigate to the directory with `cd virtual-vacation`
3. Create a virtual environment with `virtualenv env`
4. Activate the virtual environment with `source env/bin/activate`
6. Install all requirements with `pip3 install -r requirements.txt`
7. Next, run `python3 seed_database.py`
8. Finally, launch the server with `python3 server.py`
9. Open http://localhost:5000/ to view the site!

# Testing
To run tests for Virtual Vacation please follow these steps: 

1. Ensure you've downloaded coverage with the requirements, if not run: `pip3 install coverage`
2. In your terminal, run tests via coverage with `coverage run --source=. --omit="env/*" tests.py`. This will exclude testing the virutal environment. 
3. For a report, run `coverage report -m`

## Coming Soon...
A few ideas of features to add in the future: 
- Improve flow for saving images so they're not saved in the project directory
- Add user flow to allow folks to create profiles and save images privately
- Add ability for users to add new destinations and collections 