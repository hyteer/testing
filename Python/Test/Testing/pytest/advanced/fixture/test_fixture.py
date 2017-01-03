smtpserver = "mail.python.org"  # will be read by smtp2 fixture

def test_showhelo(smtp_v2):
    assert 0, smtp_v2.helo()
