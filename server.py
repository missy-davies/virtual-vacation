"""Server for Virtual Vacation image repository"""

from flask import Flask, render_template, request, flash, redirect, url_for
import jinja2
from werkzeug.utils import secure_filename

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


@app.route('/destinations/<destination_id>')
def show_gallery(destination_id):
    """Display page for each destination with images"""
 
    destination = crud.get_destination_by_id(destination_id)
    destination_images = crud.get_images_by_destination(destination)

    return render_template('destination-details.html', destination=destination,
                                                       destination_images=destination_images)


UPLOAD_FOLDER = "./static/img/uploads"
ALLOWED_EXTENSIONS = {'jpeg', 'jpg', 'png'}

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


# From Flask documentation on uploading files https://flask.palletsprojects.com/en/1.1.x/patterns/fileuploads/
def allowed_file(filename):
    """Check if file type is an image and supported"""

    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def save_file():
    """Save image to database based on destination selected"""
    
    name = request.form.get('destination')
    destination = Destination.query.filter_by(name=name).one()
    url = request.files['file'].filename

    crud.create_image(url, destination)
    db.session.commit()

    return redirect('/upload') 


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():

    destinations = crud.return_destinations()
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            save_file()
            return redirect(url_for('upload_file', filename=filename))

    return render_template('upload.html', destinations=destinations)


#------------------------------------------------------------------#

if __name__ == "__main__":
    connect_to_db(app)
    app.run(debug=True, host="0.0.0.0")