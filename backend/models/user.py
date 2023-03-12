from .mixins import HasTimestamps
from app import db

table_name = 'users'


class User(HasTimestamps, db.Model):
    __tablename__ = table_name

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String)

    status_id = db.Column(db.ForeignKey('statuses.id'), nullable=False)
