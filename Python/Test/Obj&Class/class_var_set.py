
class Config:

    MYSQL_CONFIG = {
        'host': '192.168.198.128',
        'user': 'tester',
        'passwd': '112',
        'db': 'temptest'
    }



class Mysql():
    cfg = {
    'host': '',
    'user': '',
    'passwd': '',
    'db': ''
    }
    conn = None
    cur = None

    def set_cfg(self,config):
        cfg = config.MYSQL_CONFIG
        self.cfg['host'] = cfg['host']
        self.cfg['user'] = cfg['user']
        self.cfg['passwd'] = cfg['passwd']
        self.cfg['db'] = cfg['db']
        print "init mysql config with success..."


config = Config()

mydb = Mysql()
mydb.set_cfg(config)
print "user",mydb.cfg['user']
