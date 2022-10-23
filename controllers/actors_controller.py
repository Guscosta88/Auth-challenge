from flask import Blueprint
from db import db
from models.actor import Actor
from schemas.actor_schema import ActorSchema

actors_bp = Blueprint('actors', __name__, url_prefix='/actors')

@actors_bp.route('/')
# @jwt_required()
def all_actors():
    #to test
    # return 'all_cards route'

    # if not authorize():
    #     return {'error': 'You must be an admin'}, 401
    stmt = db.select(Actor).order_by(Actor.priority.desc(), Actor.title)
    actors = db.session.scalars(stmt)
    return ActorSchema(many=True).dump(actors)

@actors_bp.route('/<int:id>/')
def one_actor(id):
    stmt = db.select(Actor).filter_by(id=id)
    actor = db.session.scalar(stmt)
    return ActorSchema().dump(actor)
