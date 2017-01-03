# content of test_sample.py
import pytest

def inc(x):
    return x + 1

def mymax(x,y):
    return max(x,y)

def test_answer_wrong():
    assert inc(3) == 5

def test_answer_right():
    import pdb
    pdb.set_trace()
    print dir(pytest)
    assert inc(3) == 4