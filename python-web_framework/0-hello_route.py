#!/usr/bin/python3
"""a script that starts a Flask web application:
"""
from flask import Flask

app = Flask(__name__, host="0.0.0.0", port=5000)


@app.route("/", strict_slashes=False)
def hello():
    return "Hello HBNB!"
