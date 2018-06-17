from sqlalchemy import Column
from server import db


class City(db().Model):
    """Represent particular city."""

    id: Column = db().Column(db().Integer, primary_key=True)
    name: Column = db().Column(db().String(50), nullable=False)
