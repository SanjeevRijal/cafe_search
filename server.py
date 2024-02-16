from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500),nullable=False)
    map_url = db.Column(db.String(500),nullable=False)
    img_url = db.Column(db.String(500),nullable=False)
    location = db.Column(db.String(250), nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    coffee_price = db.Column(db.String(250), nullable=False)


filter_option = []


@app.route("/filter<value>", methods = ["POST", "GET"])
def data(value):
    if value not in filter_option:
        filter_option.append(value)
    elif value in filter_option:
        filter_option.remove(value)
    # Construct the filter query dynamically#
    filter_conditions = [getattr(cafe, column) == True for column in filter_option]
    data = cafe.query.filter(*filter_conditions).all()
    return render_template("index.html", data =data )


@app.route("/")
def home():
    data = cafe.query.all()
    return render_template("index.html", data = data)

if __name__ == '__main__':
    app.run(debug=True)