import pytest

# normal way
def test_raises():
    print "raises test"
    with pytest.raises(ZeroDivisionError):
        1/0
    print "ZeroDivError: ", ZeroDivisionError
    assert ZeroDivisionError

def test_raises2():
    val = 11
    with pytest.raises(ValueError) as exc_info:
        if val > 10:
            raise ValueError("value must be <= 10")
    assert str(exc_info.value) == "value must be <= 10"

# lambda way
def test_raises_lambda():
    pytest.raises(ZeroDivisionError, lambda: 1/0)

# arbitrary function way
def f(x): return 1/x
def test_raises_fun():
    pytest.raises(ZeroDivisionError, f, 0)
    assert ZeroDivisionError

# use a string to be executed
def test_raises_str():
    pytest.raises(ZeroDivisionError, "f(0)")








