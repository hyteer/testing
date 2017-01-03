# content of test_some_are_slow.py
import time

def test_funcfast():
    pass

def test_funcslow1():
    time.sleep(0.1)

def test_funcslow2():
    time.sleep(0.2)