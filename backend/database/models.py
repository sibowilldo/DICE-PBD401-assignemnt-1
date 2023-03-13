import os
from sqlalchemy import Column, String, Integer, SmallInteger, Text, DateTime, ForeignKey
from flask_sqlalchemy import SQLAlchemy
import json
from dotenv import load_dotenv

from database.mixins import HasTimestamps

load_dotenv('../../.env')

database = os.getenv('DATABASE_NAME')
project_dir = os.path.dirname(os.path.abspath(__file__))
database_path = f'{os.getenv("DB_CONNECTION", "")}://{os.getenv("DB_USERNAME")}:' \
                f'{os.getenv("DB_PASSWORD", "")}@{os.getenv("DB_HOST")}:' \
                f'{os.getenv("DB_PORT")}/{os.getenv("DB_DATABASE")}'

db = SQLAlchemy()


def setup_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)


class Status(HasTimestamps, db.Model):
    __tablename__ = 'statuses'

    id = Column(Integer, primary_key=True)
    model_type = Column(String)
    name = Column(String)
    description = Column(String(500), nullable=True)
    priority = Column(SmallInteger(), nullable=True, default=None)


class Category(HasTimestamps, db.Model):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(Text, nullable=True)


class Type(HasTimestamps, db.Model):
    __tablename__ = 'types'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(Text, nullable=True)


class User(HasTimestamps, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String)

    status_id = db.Column(db.ForeignKey('statuses.id'), nullable=False)


class Profile(HasTimestamps, db.Model):
    __tablename__ = 'profiles'

    id = Column(Integer, primary_key=True)
    given_name = Column(String)
    family_name = Column(String)
    name = Column(String)

    user_id = Column(ForeignKey('users.id'), nullable=False)


class Vacancy(HasTimestamps, db.Model):
    __tablename__ = 'vacancies'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(Text)
    department = Column(String)
    location = Column(String)
    expires_at = Column(DateTime, nullable=True)

    user_id = Column(ForeignKey('users.id'), nullable=False)
    category_id = Column(ForeignKey('categories.id'), nullable=False)
    type_id = Column(ForeignKey('types.id'), nullable=False)

    def short(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description
        }

    def long(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def __repr__(self):
        return json.dumps(self.short())


class Application(HasTimestamps, db.Model):
    __tablename__ = 'applications'

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('users.id'), nullable=False)
    status_id = Column(ForeignKey('users.id'), nullable=False)
    vacancy_id = Column(ForeignKey('vacancies.id'), nullable=False)


class Attachment(HasTimestamps, db.Model):
    __tablename__ = 'attachments'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=True, default=None)
    path = Column(String, nullable=False)
    type = Column(String, nullable=False)
    mime_type = Column(String, nullable=False)

    application_id = Column(ForeignKey('applications.id'), nullable=False)
