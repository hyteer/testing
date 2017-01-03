def test_env(conf):
    cfg = conf
    print("Flag:",cfg.INIT_FLAG)
    print "\nTestEnv:%s" % cfg.ENV
    assert 1

def test_config(conf):
    cfg = conf
    print "\nmember_id:%s" % cfg.MEMBER_ID
    print "user_id:%s" % cfg.USER_ID
    print "Env:",cfg.ENV

