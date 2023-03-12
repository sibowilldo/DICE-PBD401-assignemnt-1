from app import db, datetime
from sqlalchemy.ext.declarative import declared_attr


class TimestampsMixin(object):
    @declared_attr
    def created_at(self):
        return db.Column(db.DateTime, default=datetime.now(), nullable=False)

    @declared_attr
    def updated_at(self):
        return db.Column(db.DateTime, onupdate=datetime.now(), nullable=True)


HasTimestamps = TimestampsMixin
