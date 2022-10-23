from db import ma
from models.actor import Actor

class ActorSchema(ma.Schema):
    class Meta:
        fields = ("id", "first_name", "last_name", "gender", "country")

actor_schema = ActorSchema()
actors_schema = ActorSchema(many=True)