from .mixins import HasTimestamps
from app import db

table_name = 'categories'


class Category(HasTimestamps, db.Model):
    __tablename__ = table_name

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.Text, nullable=True)
