#!/usr/bin/python3
""" 10. States and State """
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.amenity import Amenity
app = Flask(__name__)


@app.teardown_appcontext
def teardown(close):
    """ remove current session """
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def states(id='0'):
    """ displays all states in an HTML page """
    return render_template('10-hbnb_filters.html',
                           states=storage.all(State).values(),
                           amenities=storage.all(Amenity).values(), id=id)

if __name__ == '__main__':
    storage.reload()
    app.run(host='0.0.0.0', port=5000)
