import os
from sqlalchemy import Column, String, Integer, SmallInteger, Text, DateTime, ForeignKey, Boolean
from flask_sqlalchemy import SQLAlchemy

from dotenv import load_dotenv
from flask import jsonify
from flask_login import UserMixin

from app import db

from .mixins import HasTimestamps, json


class Status(HasTimestamps, db.Model):
    __tablename__ = 'statuses'

    id = Column(Integer, primary_key=True)
    model_type = Column(String)
    name = Column(String)
    description = Column(String(500), nullable=True)
    priority = Column(SmallInteger(), nullable=True, default=None)

    applications = db.relationship(
        'Application', backref='status', lazy=True, cascade='all, delete')

    def short(self):
        return {
            'id': self.id,
            'name': self.name,
            'model_type': self.model_type,
            'priority': self.priority,
        }

    def long(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'model_type': self.model_type,
            'priority': self.priority,
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


class Category(HasTimestamps, db.Model):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(Text, nullable=True)

    vacancies = db.relationship(
        'Vacancy', backref='category', lazy=True, cascade='all, delete')

    def short(self):
        return {
            'id': self.id,
            'name': self.name,
        }

    def long(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'created_at': self.created_at,
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


class Type(HasTimestamps, db.Model):
    __tablename__ = 'types'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(Text, nullable=True)

    vacancies = db.relationship(
        'Vacancy', backref='type', lazy=True, cascade='all, delete')

    def short(self):
        return {
            'id': self.id,
            'name': self.name,
        }

    def long(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'created_at': self.created_at,
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


class User(UserMixin, HasTimestamps, db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)
    is_active = Column(Boolean, default=False)

    status_id = Column(ForeignKey('statuses.id'), nullable=False)

    vacancies = db.relationship(
        'Vacancy', backref='user', lazy=True, cascade='all, delete')

    applications = db.relationship(
        'Application', backref='user', lazy=True, cascade='all, delete')

    profile = db.relationship("Profile", uselist=False, back_populates="user")

    def short(self):
        return {
            'id': self.id,
            'email': self.email,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'profile': self.profile.short()
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


class Profile(HasTimestamps, db.Model):
    __tablename__ = 'profiles'

    id = Column(Integer, primary_key=True)
    given_name = Column(String)
    family_name = Column(String)
    name = Column(String)
    picture = Column(String, nullable=True, default=None)
    user_id = Column(ForeignKey('users.id'), nullable=False)
    user = db.relationship("User", back_populates="profile")

    def short(self):
        return {
            'id': self.id,
            'given_name': self.given_name,
            'family_name': self.family_name,
            'name': self.name,
            'picture': self.picture,
            'composed_name': f'{self.family_name}, {self.given_name}'
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


    applications = db.relationship(
        'Application', backref='vacancy', lazy=True, cascade='all, delete')

    def short(self):
        return {
            'id': self.id,
            'title': self.title,
            'department': self.department,
            'description': self.description[0:50],
            'location': self.location,
            'expires_at': self.expires_at,
            'user': self.user.short()
        }

    def long(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description[0:150],
            'department': self.department,
            'location': self.location,
            'expires_at': self.expires_at,
            'created_at': self.created_at,
            'user': self.user.short(),
            'category': self.category.short(),
            'type': self.type.short(),
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
    status_id = Column(ForeignKey('statuses.id'), nullable=False)
    vacancy_id = Column(ForeignKey('vacancies.id'), nullable=False)

    def short(self):
        return {
            'id': self.id,
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


class Attachment(HasTimestamps, db.Model):
    __tablename__ = 'attachments'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=True, default=None)
    path = Column(String, nullable=False)
    type = Column(String, nullable=False)
    mime_type = Column(String, nullable=False)

    application_id = Column(ForeignKey('applications.id'), nullable=False)

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
