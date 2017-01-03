str = 'sally'

def contains(x):
    return x + 'l'

def test_contains_ind():
    x = 'sa'
    y = 'sally'
    assert x in y

def test_contains():
    assert contains('sil') in str
