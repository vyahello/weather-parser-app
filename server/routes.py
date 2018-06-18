from typing import List, Any, Dict
from server import weather, db
from server.city import City
from server.forecast.forecasts import WeatherForecast
from server.storage.sessions import ClientSession
from server.view.requests import Request, ViewRequest
from server.view.templates import WeatherTemplate

_root: str = '/'
_GET_METHOD: str = 'GET'
_POST_METHOD: str = 'POST'
_weather_template: str = 'weather.html'
_city: str = 'city'


@weather.route(_root, methods=[_GET_METHOD, _POST_METHOD])
def home():
    weather_data: List[Dict[Any, Any]] = []
    cities: List[City] = City.query.all()
    req: Request = ViewRequest(db_table_name=_city)

    if req.method() == _POST_METHOD:
        new_city: str = req.get()
        if new_city:
            ClientSession(db, City(name=new_city)).add()

    for city in cities:
        weather_data.append(WeatherForecast(city).latest())

    return WeatherTemplate(_weather_template).render(weather_data=weather_data)
