from .mixins import HasTimestamps
from app import db

table_name = 'applications'


class Application(HasTimestamps, db.Model):
    __tablename__ = table_name

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.ForeignKey('users.id'), nullable=False)
    status_id = db.Column(db.ForeignKey('users.id'), nullable=False)
    vacancy_id = db.Column(db.ForeignKey('vacancies.id'), nullable=False)
