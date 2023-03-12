from .mixins import HasTimestamps
from app import db

table_name = 'statuses'


class Artist(HasTimestamps, db.Model):
    __tablename__ = table_name

    id = db.Column(db.Integer, primary_key=True)
    model_type = db.Column(db.String)
    name = db.Column(db.String)
    description = db.Column(db.String(500), nullable=True)
    priority = db.Column(db.SmallInteger(), nullable=True, default=None)
