from sqlalchemy import inspect
from datetime import datetime

from ... import db # from __init__.py

# ----------------------------------------------- #

class Account(db.Model):
# Auto Generated Fields:
    id           = db.Column(db.String(50), primary_key=True, nullable=False, unique=True)
    created      = db.Column(db.DateTime(timezone=True), default=datetime.now)                           # The Date of the Instance Creation => Created one Time when Instantiation
    updated      = db.Column(db.DateTime(timezone=True), default=datetime.now, onupdate=datetime.now)    # The Date of the Instance Update => Changed with Every Update

# Input by User Fields:
    email        = db.Column(db.String(100), nullable=False, unique=True)
    username     = db.Column(db.String(100), nullable=False)
    birth_date          = db.Column(db.Date)
    phone_number = db.Column(db.String(20))


# Set an empty string to null for username field
    def empty_string_to_null(self, key, value):
        if isinstance(value, str) and value == '': return None
        else: return value


# How to serialize SqlAlchemy PostgreSQL Query to JSON
    def toDict(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }
    
    def __repr__(self):
        return "<%r>" % self.email