from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column
from server import db

_db: SQLAlchemy = db.synchronize()


class City(_db.Model):
    """Represent particular city."""

    id: Column = _db.Column(_db.Integer, primary_key=True)
    name: Column = _db.Column(_db.String(50), nullable=False)
