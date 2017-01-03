smtpserver = "mail.python.org"  # will be read by smtp2 fixture

from conftest import smtp_v3 as smtp

def test_showhelo(smtp_v3):
    assert 0, smtp_v3.helo()

def test_showhelo2(smtp):
    assert 0, smtp.helo()

def test_noop(smtp):
    response, msg = smtp.noop()
    assert response == 250
