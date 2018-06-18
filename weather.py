from server import weather

_host: str = 'localhost'
_port: int = 5050

if __name__ == '__main__':
    weather.run(host=_host, port=_port)
