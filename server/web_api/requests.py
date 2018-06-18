from abc import ABC, abstractmethod
from typing import Dict, Any
import requests
from server.web_api.responses import Response, HttpResponse, HttpResponseError


class Session(ABC):
    """The abstraction of a specific session."""

    @abstractmethod
    def get(self) -> Response:
        pass


class Request(ABC):
    """The abstraction of a specific API request."""

    @abstractmethod
    def response(self) -> Response:
        pass


class _ApiSession(Session):
    """The abstraction of a specific API session."""

    def __init__(self, url: str, **options: Dict[Any, Any]) -> None:
        self._session: requests.Session = requests.Session()
        self._url = url
        self._options = options

    def get(self) -> Response:
        return HttpResponse(self._session.get(self._url, **self._options, verify=False))


class Get(Request):
    """Represent ``GET`` API request."""

    def __init__(self, url: str, **options: Dict[Any, Any]) -> None:
        self._session: Session = _ApiSession(url, **options)

    def response(self) -> Response:
        return self._session.get()


class SafeGet(Request):
    """Represent safe `GET` API request that expects `200` status code."""

    def __init__(self, url: str, status_code: int = 200, **options: Dict[Any, Any]) -> None:
        self._get: Request = Get(url, **options)
        self._status_code = status_code

    def response(self) -> Response:
        response: Response = self._get.response()
        if response.status_code() != self._status_code:
            raise HttpResponseError(f'HTTP response error with {response.status_code()} status code!!!')
        return response
