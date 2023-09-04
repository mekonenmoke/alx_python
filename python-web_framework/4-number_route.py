#!/usr/bin/python3
"""a script that starts a Flask web application:
"""
from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello():
    return "Hello HBNB!"
@app.route("/hbnb", strict_slashes=False)
def hbn():
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def c(text):
    return "C %s" % text

@app.route("/python", strict_slashes=False)
@app.route("/python/text/<int:text>", strict_slashes=False)
def python(text = "is cool"):
    return "Python_%s" % text

@app.route("/number/<n>", strict_slashes=False)
def number(n):
    if type(n) is int:
        return "%s is a number" % n


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
