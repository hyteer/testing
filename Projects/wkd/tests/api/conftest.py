import pytest
import datetime
import smtplib

@pytest.fixture(scope="session")
def debug_teardown(request):
    print("Use session fixture:",datetime.datetime.now())
    def teardown():
        print("Teardown...")
        print("Finished...")
        print("Time:",datetime.datetime.now())
    request.addfinalizer(teardown)
    return datetime.datetime.now()



@pytest.fixture(scope="module")
def smtp(request):
    smtp = smtplib.SMTP("smtp.qq.com")
    def fin():
        print ("teardown smtp")
        smtp.close()
    request.addfinalizer(fin)
    return smtp  # provide the fixture value

@pytest.fixture(scope="module")
def smtp2(request):
    smtp = smtplib.SMTP("smtp.qq.com")
    yield smtp  # provide the fixture value
    print("teardown smtp2")
    smtp.close()

