from datetime import datetime
from sqlalchemy import Column, DateTime
from sqlalchemy.ext.declarative import declared_attr
import json

class TimestampsMixin(object):
    @declared_attr
    def created_at(self):
        return Column(DateTime, default=datetime.now(), nullable=False)

    @declared_attr
    def updated_at(self):
        return Column(DateTime, onupdate=datetime.now(), nullable=True)

HasTimestamps = TimestampsMixin