from .mixins import HasTimestamps
from app import db

table_name = 'profiles'


class Profile(HasTimestamps, db.Model):
    __tablename__ = table_name

    id = db.Column(db.Integer, primary_key=True)
    given_name = db.Column(db.String)
    family_name = db.Column(db.String)
    name = db.Column(db.String)

    user_id = db.Column(db.ForeignKey('users.id'), nullable=False)
