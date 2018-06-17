from abc import ABC, abstractmethod
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import scoped_session


class DB(ABC):
    """Represent abstraction for a database."""

    @abstractmethod
    def session(self) -> scoped_session:
        pass

    @abstractmethod
    def __call__(self) -> SQLAlchemy:
        pass


class SqlDB(DB):
    """Represent concrete SQL DB."""

    def __init__(self, server: Flask) -> None:
        self._db = SQLAlchemy(server)

    def session(self) -> scoped_session:
        return self._db.session

    def __call__(self) -> SQLAlchemy:
        return self._db
