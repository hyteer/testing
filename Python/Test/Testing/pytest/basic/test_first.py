# content of test_sample.py
def inc(x):
    return x + 1

def mymax(x,y):
    return max(x,y)

def test_answer_wrong():
    assert inc(3) == 5

def test_answer_right():
    assert inc(3) == 4

def test_max_right():
    assert mymax(3,8) == 8

def test_max_wrong():
    assert mymax(3,8) == 3

def test_max_illegal():
    assert mymax(3,8) == 5
