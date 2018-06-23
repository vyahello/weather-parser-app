from abc import ABC, abstractmethod
from typing import Dict, Any, Callable
from server.city import City
from server.forecast import URL, APP_ID
from server.web_api.requests import Request, SafeGet


class Forecast(ABC):
    """The abstraction of a specific forecast."""

    @abstractmethod
    def latest(self) -> Dict[str, Any]:
        pass


class WeatherForecast(Forecast):
    """Represent of a specific weather forecast."""

    def __init__(self, city: City) -> None:
        self._city: City = city
        self._req: Callable[[City], Request] = lambda ct: SafeGet(url=URL.format(ct.name, APP_ID))

    def latest(self) -> Dict[str, Any]:
        data = self._req(self._city).response().json()

        return {
            'city': self._city.name,
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon'],
        }
