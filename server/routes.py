from typing import List, Any
import requests
from flask import render_template
from server import weather, db
from server.city import City
from server.storage.sessions import ClientSession
from server.view.requests import Request, ViewRequest

_root: str = '/'

_GET_METHOD: str = 'GET'
_POST_METHOD: str = 'POST'

_url: str = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=271d1234d3f497eed5b1d80a07b3fcd1'
_weather_template: str = 'weather.html'


@weather.route(_root, methods=[_GET_METHOD, _POST_METHOD])
def home():
    weather_data: List[Any] = []
    cities: List[City] = City.query.all()
    req: Request = ViewRequest(db_table_name='city')

    if req.method() == _POST_METHOD:
        new_city: str = req.get()
        if new_city:
            ClientSession(db, City(name=new_city)).add()

    for city in cities:
        r = requests.get(_url.format(city.name)).json()

        forecast = {
            'city': city.name,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
        }

        weather_data.append(forecast)

    return render_template(_weather_template, weather_data=weather_data)
