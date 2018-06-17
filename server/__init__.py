from flask import Flask
from server.servers import WeatherApp
from server.storage.db import SqlDB, DB

weather: Flask = WeatherApp()
weather.configure()
db: DB = SqlDB(weather)

from server import routes
