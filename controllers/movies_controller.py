from flask import Blueprint, request
from init import db
from datetime import date
from models.movie import Movie, MovieSchema
from controllers.auth_controller import authorize
from flask_jwt_extended import jwt_required


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
    if movie:
        return MovieSchema().dump(movie)
    else:
        return {'error': f'Movie not found with id {id}'}, 404

@movies_bp.route('/<int:id>/', methods=['DELETE'])
@jwt_required()
def delete_one_movie(id):
    authorize()

    stmt = db.select(Movie).filter_by(id=id)
    movie = db.session.scalar(stmt)
    if card:
        db.session.delete(movie)
        db.session.commit()
        return {'message': f'Movie "{movie.title}" deleted successfully'}
    else:
        return {'error': f'Movie not found with id {id}'}, 404

@movies_bp.route('/<int:id>/', methods=['PUT', 'PATCH'])
@jwt_required()
def update_one_movie(id):
    stmt = db.select(Movie).filter_by(id=id)
    movie = db.session.scalar(stmt)
    if movie:
        movie.title = request.json.get('title') or movie.title
        movie.genre = request.json.get('genre') or movie.genre
        movie.length = request.json.get('length') or movie.length
        movie.year = request.json.get('year') or movie.year
        db.session.commit()
        return MovieSchema().dump(movie)
    else:
        return {'error': f'Movie not found with id {id}'}, 404

@movies_bp.route('/', methods=['POST'])
@jwt_required()
def create_movie():
        movie = Movie(
            title = request.json['title'],
            genre = request.json['genre'],
            date = date.today(),
            length = request.json['length'],
            year = request.json['year']
        )

        db.session.add(movie)
        db.session.commit()

        return MovieSchema().dump(movie), 201
