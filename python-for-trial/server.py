
from flask import Flask, render_template, request
from models import GeneralProduction
from connection import database, session

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Flask"

@app.route("/products", methods = ["GET", "POST"])
def products():
    name = request.form["productname"]
    description = request.form["productdescription"]
    product = GeneralProduction(name, description)
    session.add(product)
    session.commit()


    products = session.query().all()

    return render_template("product.html", products = products)

@app.route("/about", methods = ["POST", "GET"])
def about():
    return  render_template("about.html")
if __name__ == "__main__":
    app.run(debug=True)