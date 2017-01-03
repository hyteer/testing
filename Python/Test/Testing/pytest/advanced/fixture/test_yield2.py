import pytest
import os

@pytest.fixture
def users():
    cur_path = os.path.dirname(__file__)
    res_path = os.path.join(cur_path,'res/users.txt')
    with open(res_path) as f:
        user = f.readlines()
        print user
        return user

def test_has_lines(users):
    assert len(users) >= 1