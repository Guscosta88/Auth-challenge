from flask import Blueprint
from db import db
from models.user import User
from schemas.user_schema import UserSchema


users_bp = Blueprint('users', __name__, url_prefix='/users')

@users_bp.route('/')
def all_users():
    stmt = db.select(User).order_by(User.priority.desc(), User.title)
    users = db.session.scalars(stmt)
    return UserSchema(many=True).dump(users)

@users_bp.route('/<int:id>/')
def one_user(id):
    stmt = db.select(User).filter_by(id=id)
    user = db.session.scalar(stmt)
    return UserSchema().dump(user)
