from db import db, ma, bcrypt, jwt
from flask import Flask, jsonify
app = Flask(__name__)



## DB CONNECTION AREA

from flask_sqlalchemy import SQLAlchemy 
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://trello_dev:password123@localhost:5432/ripe_tomatoes_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


# CLI COMMANDS AREA

@app.cli.command("create")
def create_db():
    db.create_all()
    print("Tables created")

@app.cli.command("seed")
def seed_db():

    movie1 = Movie(
        title = "Spider-Man: No Way Home",
        genre = "Action",
        length = 148,
        year = 2021
    )
    db.session.add(movie1)

    movie2 = Movie(
        title = "Dune",
        genre = "Sci-fi",
        length = 155,
        year = 2021
    )
    db.session.add(movie2)

    actor1 = Actor(
        first_name = "Tom",
        last_name = "Holland",
        gender = "male",
        country = "UK"
    )
    db.session.add(actor1)

    actor2 = Actor(
        first_name = "Marisa",
        last_name = "Tomei",
        gender = "female",
        country = "USA"
    )
    db.session.add(actor2)

    actor3 = Actor(
        first_name = "Timothee",
        last_name = "Chalemet",
        gender = "male",
        country = "USA"
    )
    db.session.add(actor3)

    actor4 = Actor(
        first_name = "Zendaya",
        last_name = "",
        gender = "female",
        country = "USA"
    )
    db.session.add(actor4)

    user1 = User(
        username = "Pato Banton",
        password=bcrypt.generate_password_hash('123456').decode('utf-8'),
    )
    db.session.add(user1)

    user2 = User(
        username = "Gus Costa",
        password=bcrypt.generate_password_hash('eggs').decode('utf-8'),
    )
    db.session.add(user2)
   
    db.session.commit()
    print("Tables seeded") 

@app.cli.command("drop")
def drop_db():
    db.drop_all()
    print("Tables dropped") 

# ROUTING AREA

@app.route("/")
def hello():
  return "Welcome to Ripe Tomatoes API"

@app.route("/movies", methods=["GET"])
def get_movies():
    movies_list = Movie.query.all()
    result = movies_schema.dump(movies_list)
    return jsonify(result)

@app.route("/actors", methods=["GET"])
def get_actors():
    actors_list = Actor.query.all()
    result = actors_schema.dump(actors_list)
    return jsonify(result)

@app.route("/users", methods=["GET"])
def get_users():
    users_list = User.query.all()
    result = users_schema.dump(users_list)
    return jsonify(result)