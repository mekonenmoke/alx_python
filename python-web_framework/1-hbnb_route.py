#!/usr/bin/python3
"""a script that starts a Flask web application:
"""
from flask import Flask

app = Flask(__name__)


@app.route("/hbn", strict_slashes=False)
def hbn():
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
