# content of conftest.py
import pytest
import smtplib
import os
import tempfile
"""
Test Config file...

"""

class MyConf():
    """
    Description: My test config file
    created time: 20161230
    """
    flag = False
    USERNAME = '20161210'

@pytest.fixture(scope="module")
def smtp():
    smtp = smtplib.SMTP("smtp.qq.com")
    #return smtp
    yield smtp
    print("tear down smtp...")
    smtp.close()

@pytest.fixture(scope="module")
def smtp_v2(request):
    server = getattr(request.module, "smtpserver", "smtp.qq.com")
    smtp = smtplib.SMTP(server)
    yield smtp
    print ("finalizing %s (%s)" % (smtp, server))
    smtp.close()

@pytest.fixture(scope="module",
                params=["smtp.qq.com", "mail.python.org"])
def smtp_v3(request):
    smtp = smtplib.SMTP(request.param)
    yield smtp
    print ("finalizing %s" % smtp)
    smtp.close()

# tempfile
@pytest.fixture()
def cleandir():
    newpath = tempfile.mkdtemp()
    os.chdir(newpath)

