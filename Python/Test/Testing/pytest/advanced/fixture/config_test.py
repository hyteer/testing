def test_config():
    print("Test Config...")
    #import pdb
    #pdb.set_trace()
    from conftest import MyConf
    cfg = MyConf()
    dir(cfg.USERNAME)
