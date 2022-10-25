from init import db, ma

class Actor(db.Model):
    __tablename__= "ACTORS"
    id = db.Column(db.Integer,primary_key=True)  
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    gender = db.Column(db.String())
    country = db.Column(db.String())


class ActorSchema(ma.Schema):
    class Meta:
        fields = ("id", "first_name", "last_name", "gender", "country")
        ordered = True
# actor_schema = ActorSchema()
# actors_schema = ActorSchema(many=True)