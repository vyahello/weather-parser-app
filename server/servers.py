from flask import Flask


class WeatherApp(Flask):
    """Represent flask web server."""

    def __init__(self, name: str = __name__) -> None:
        super().__init__(name)

    def configure(self) -> None:
        self.config['SECRET_KEY'] = '162733453f65d810e82eb8d5a53e898b'
        self.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather.db'
