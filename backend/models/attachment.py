from .mixins import HasTimestamps
from app import db

table_name = 'attachments'


class Attachment(HasTimestamps, db.Model):
    __tablename__ = table_name

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.Text, nullable=True, default=None)
    path = db.Column(db.String, nullable=False)
    type = db.Column(db.String, nullable=False)
    mime_type = db.Column(db.String, nullable=False)

    application_id = db.Column(db.ForeignKey('applications.id'), nullable=False)
