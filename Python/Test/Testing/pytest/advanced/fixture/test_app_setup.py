# content of test_appsetup.py

import pytest

class App:
    def __init__(self, smtp_v3):
        self.smtp = smtp_v3

@pytest.fixture(scope="module")
def app(smtp):
    return App(smtp)

def test_smtp_exists(app):
    assert app.smtp