# content of tests/conftest.py

#import time
#from selenium import webdriver
#from selenium.webdriver.support.ui import WebDriverWait
import pytest
from operations.common import login,float_compare
from config import WshConfig,get_config
cfg = WshConfig()


@pytest.fixture
def username():
    return '20161210'

@pytest.fixture
def wsh_conf():
    return cfg

@pytest.fixture
def get_conf():
    return get_config

@pytest.fixture
def wsh_login():
    return login

@pytest.fixture
def float_comp():
    return float_compare
