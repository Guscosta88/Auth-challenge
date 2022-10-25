from flask import Blueprint, request
from init import db
from datetime import date
from models.actor import Actor, ActorSchema
from controllers.auth_controller import authorize
from flask_jwt_extended import jwt_required

actors_bp = Blueprint('actors', __name__, url_prefix='/actors')


@actors_bp.route('/')
def all_actors():
    stmt = db.select(Actor).order_by(Actor.priority.desc(), Actor.title)
    actors = db.session.scalars(stmt)
    return ActorSchema(many=True).dump(actors)

@actors_bp.route('/<int:id>/')
def one_actor(id):
    stmt = db.select(Actor).filter_by(id=id)
    actor = db.session.scalar(stmt)
    if actor:
        return ActorSchema().dump(actor)
    else:
        return {'error': f'Actor not found with id {id}'}, 404

@actors_bp.route('/<int:id>/', methods=['DELETE'])
@jwt_required()
def delete_one_actor(id):
    authorize()

    stmt = db.select(Actor).filter_by(id=id)
    actor = db.session.scalar(stmt)
    if actor:
        db.session.delete(actor)
        db.session.commit()
        return {'message': f'Actor "{actor.first_name}" deleted successfully'}
    else:
        return {'error': f'Movie not found with id {id}'}, 404

@actors_bp.route('/<int:id>/', methods=['PUT', 'PATCH'])
@jwt_required()
def update_one_actor(id):
    stmt = db.select(Actor).filter_by(id=id)
    actor = db.session.scalar(stmt)
    if actor:
        actor.first_name = request.json.get('first_name') or actor.first_name
        actor.last_name = request.json.get('last_name') or actor.last_name
        actor.gender = request.json.get('gender') or actor.gender
        actor.country = request.json.get('country') or actor.country
        db.session.commit()
        return ActorSchema().dump(actor)
    else:
        return {'error': f'Actor not found with id {id}'}, 404

@actors_bp.route('/', methods=['POST'])
@jwt_required()
def create_actor():
        actor = Actor(
            first_name = request.json['first_name'],
            last_name = request.json['last_name'],
            date = date.today(),
            gender = request.json['gender'],
            country = request.json['country']
        )

        db.session.add(actor)
        db.session.commit()

        return ActorSchema().dump(actor), 201