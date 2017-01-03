# content of ./test_smtpsimple.py
import pytest

qq = "smtp.qq.com"
gmail = "smtp.gmail.com"
provider = qq

@pytest.fixture
def smtp():
    global provider
    import smtplib
    return smtplib.SMTP(provider)

def test_ehlo(smtp):
    response, msg = smtp.ehlo()
    print msg
    assert response == 250
    #assert 0 # for demo purposes