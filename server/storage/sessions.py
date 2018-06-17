from abc import ABC, abstractmethod
from server.city import City
from server.storage.db import DB


class Session(ABC):
    """Represent abstraction of database session."""

    @abstractmethod
    def add(self) -> None:
        pass


class ClientSession(Session):
    """Represent concrete database session."""

    def __init__(self, db: DB, city: City) -> None:
        self._db = db
        self._city = city

    def add(self) -> None:
        self._db.session().add(self._city)
        self._db.session().commit()
