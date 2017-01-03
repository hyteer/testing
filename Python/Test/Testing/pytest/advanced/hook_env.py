# content of test_sample.py
def inc(x):
    return x + 1

def mymax(x,y):
    return max(x,y)

def test_answer_wrong():
    assert inc(3) == 5

def test_answer_right():
    assert inc(3) == 4

"""
def test_getenv():

    print dir(pytest)
    pytest.register_assert_rewrite('pytest_foo.helper')
    assert True
"""