import requests
from flask import render_template, request
from server import db, weather
from server.city import City


@weather.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        new_city = request.form.get('city')

        if new_city:
            new_city_obj = City(name=new_city)

            db.session.add(new_city_obj)
            db.session.commit()

    cities = City.query.all()

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=271d1234d3f497eed5b1d80a07b3fcd1'

    weather_data = []

    for city in cities:
        r = requests.get(url.format(city.name)).json()

        forecast = {
            'city': city.name,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
        }

        weather_data.append(forecast)

    return render_template('weather.html', weather_data=weather_data)