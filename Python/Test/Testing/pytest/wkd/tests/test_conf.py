def test_username(username):
    assert username == 'overridden-20161210'

def test_config(conf):
    print "\n"
    cfg = conf("test")
    print "member_id:%s" % cfg.MEMBER_ID
    print "user_id:%s" % cfg.USER_ID
