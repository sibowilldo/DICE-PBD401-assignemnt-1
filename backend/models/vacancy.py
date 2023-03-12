from .mixins import HasTimestamps
from app import db

table_name = 'vacancies'


class Vacancy(HasTimestamps, db.Model):
    __tablename__ = table_name

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.Text)
    department = db.Column(db.String)
    location = db.Column(db.String)
    expires_at = db.Column(db.DateTime, nullable=True)

    user_id = db.Column(db.ForeignKey('users.id'), nullable=False)
    category_id = db.Column(db.ForeignKey('categories.id'), nullable=False)
    type_id = db.Column(db.ForeignKey('types.id'), nullable=False)
