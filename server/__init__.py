from flask import Flask
from flask_sqlalchemy import SQLAlchemy

weather = Flask(__name__)
weather.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather.db'
db = SQLAlchemy(weather)