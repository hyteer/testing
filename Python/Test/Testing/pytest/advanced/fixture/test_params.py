# content of test_compute.py

def test_valid_string(stringinput):
    assert stringinput.isalpha()

def test_get_env(option):

    print "Env is: %s" % option
    #assert env.isalpha()

def test_db(db):
    print db
    assert 1

def test_env(env):
    print "TestEnv:%s" % env
    assert 1
