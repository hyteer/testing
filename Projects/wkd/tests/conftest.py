
# content of tests/subfolder/conftest.py
import pytest


@pytest.fixture
def username(username):
    return 'overridden-' + username