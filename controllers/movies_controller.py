from flask import Blueprint
from db import db
from models.movie import Movie
from schemas.movie_schema import MovieSchema




movies_bp = Blueprint('movies', __name__, url_prefix='/movies')

@movies_bp.route('/')
def all_movies():
    stmt = db.select(Movie).order_by(Movie.priority.desc(), Movie.title)
    movies = db.session.scalars(stmt)
    return MovieSchema(many=True).dump(movies)

@movies_bp.route('/<int:id>/')
def one_movie(id):
    stmt = db.select(Movie).filter_by(id=id)
    movie = db.session.scalar(stmt)
    return MovieSchema().dump(movie)
