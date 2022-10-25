from flask import Blueprint
from init import db, bcrypt
from datetime import date
from models.movie import Movie
from models.actor import Actor
from models.user import User


db_commands = Blueprint('db', __name__)


@db_commands.cli.command('create')
def create_db():
    db.create_all()
    print("Tables created")

@db_commands.cli.command('drop')
def drop_db():
    db.drop_all()
    print("Tables dropped")

@db_commands.cli.command('seed')
def seed_db():
    users = [
        User(
            email='admin@spam.com',
            password=bcrypt.generate_password_hash('eggs').decode('utf-8'),
            is_admin=True
        ),
        User(
            name='John Cleese',
            email='someone@spam.com',
            password=bcrypt.generate_password_hash('12345').decode('utf-8')
        ),
        User(
            name='Gus Costa',
            email='gus@spam.com',
            password=bcrypt.generate_password_hash('12345').decode('utf-8')
        ),
        User(
            name='Pato Banton',
            email='Gopato@spam.com',
            password=bcrypt.generate_password_hash('12345').decode('utf-8')
        )
    ]

    movies = [
        Movie(
        title = "Spider-Man: No Way Home",
        genre = "Action",
        length = 148,
        year = 2021
        ),
        Movie(
        title = "Dune",
        genre = "Sci-fi",
        length = 155,
        year = 2021
        )
    ]

    actors = [
        Actor(
        first_name = "Tom",
        last_name = "Holland",
        gender = "male",
        country = "UK"
        ),
        Actor(
        first_name = "Marisa",
        last_name = "Tomei",
        gender = "female",
        country = "USA"
        ),
        Actor(
        first_name = "Timothee",
        last_name = "Chalemet",
        gender = "male",
        country = "USA"
        ),
        Actor(
        first_name = "Zendaya",
        last_name = "",
        gender = "female",
        country = "USA"
        )
    ]

    db.session.add_all(actors)
    db.session.add_all(movies)
    db.session.add_all(users)
    db.session.commit()
    print('Tables seeded')




