import pytest

_endpoint: str = 'http://localhost:5050/'
_success: int = 200


@pytest.fixture(scope='module')
def endpoint() -> str:
    return _endpoint


@pytest.fixture(scope='module')
def success() -> int:
    return _success
