#!/usr/bin/python3
""" 3. Python is cool! """

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ display Hello HBNB! """
    return("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ display HBNB """
    return("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """ display C <text> (underscores replaced by spaces) """
    return("C {}".format(text).replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """ display Python <text> (underscores replaced by spaces) """
    return("Python {}".format(text).replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
