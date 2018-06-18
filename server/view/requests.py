from abc import ABC, abstractmethod
from flask import request
from werkzeug.local import LocalProxy


class Request(ABC):
    """Represent abstraction of a request."""

    @abstractmethod
    def method(self) -> str:
        pass

    @abstractmethod
    def get(self) -> str:
        pass


class ViewRequest(Request):
    """Represent city request."""

    def __init__(self, db_table_name: str) -> None:
        self._name = db_table_name
        self._req: LocalProxy = request

    def method(self) -> str:
        return self._req.method

    def get(self) -> str:
        return self._req.form.get(self._name)
