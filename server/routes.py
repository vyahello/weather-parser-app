import requests
from flask import request, render_template
from server import weather, db
from server.city import City

_root: str = '/'

_GET_METHOD: str = 'GET'
_POST_METHOD: str = 'POST'

_url: str = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=271d1234d3f497eed5b1d80a07b3fcd1'
_weather_template: str = 'weather.html'


@weather.route(_root, methods=[_GET_METHOD, _POST_METHOD])
def home():
    if request.method == _POST_METHOD:
        new_city = request.form.get('city')

        if new_city:
            new_city_obj = City(name=new_city)

            db.session.add(new_city_obj)
            db.session.commit()

    cities = City.query.all()

    weather_data = []

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
