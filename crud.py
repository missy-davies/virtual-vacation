"""CRUD operations"""

# from model import db, connect_to_db, Destination, Image
import model 


def create_destination(name):
    """Create and return a destination"""

    destination = model.Destination(name=name)

    model.db.session.add(destination)
    model.db.session.commit()

    return destination


def create_image(url, destination):
    """Create and return an image"""

    image = model.Image(url=url, destination=destination)

    model.db.session.add(image)
    model.db.session.commit()

    return image 


def return_destinations():
    """Return destinations"""

    return model.Destination.query.all()


def get_destination_by_id(destination_id):
    """Return destination by ID"""

    return model.Destination.query.get(destination_id)


def get_images_by_destination(destination):
    """Return images given a destination object"""

    return destination.images

#------------------------------------------------------------------#

if __name__ == '__main__':
    from server import app
    model.connect_to_db(app)