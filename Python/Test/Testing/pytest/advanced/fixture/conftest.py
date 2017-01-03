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

# parameterizing
'''
def pytest_addoption(parser):
    parser.addoption("--stringinput", action="append", default=[],
        help="list of stringinputs to pass to test functions")

def pytest_generate_tests(metafunc):
    if 'stringinput' in metafunc.fixturenames:
        metafunc.parametrize("stringinput", metafunc.config.option.stringinput)

def pytest_cmdline_main(config):
    option = config.getoption('--testenv2')
    if option:
        # use the option to modify fixture data
        print "Option:%s" % option
        return option

def env_addoption(parser):
    parser.addoption("--testenv", action="store", default="test",
        help="please input a testenv,eg.'test','beta','ci'")

@pytest.fixture()
def get_env(request):
    return request.config.getoption('--testenv')
'''
def pytest_addoption(parser):
    parser.addoption("--hostname", action="store", default='127.0.0.1', help="specify IP of test host")
    parser.addoption("--testenv", action="store", default="test",help="please input a testenv,eg.'test','beta','ci'")

@pytest.fixture(scope='module')
def db(request):
    return 'CONNECTED TO [' + request.config.getoption('--hostname') + '] SUCCESSFULLY!'
@pytest.fixture(scope='session')
def env(request):
    return request.config.getoption('--testenv')






