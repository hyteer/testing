from pytest import approx

def test_float_comp():
    print "--float compare test--"
    x = 0.3
    assert 0.1+0.2 == approx(x)


