import pytest
from server.web_api.requests import SafeGet
from server.web_api.responses import Response


@pytest.fixture(scope='module')
def weather(endpoint: str) -> Response:
    return SafeGet(endpoint).response()


def test_weather_status_code(weather: Response, success: int) -> None:
    assert weather.status_code() == success


def test_weather_content(weather: Response) -> None:
    assert len(weather.content()) > 0
