# encoding:utf-8
import pymysql

cfg = {
    'host': '192.168.198.128',
    'user': 'tester',
    'passwd': '111',
    'db': 'temptest'
}

class mydb:
    def connDB(self):   #连接数据库函数     
        conn=pymysql.connect(host=cfg['host'],user=cfg['user'],passwd=cfg['passwd'],db=cfg['db'],charset='utf8')
        cur=conn.cursor()
        return (conn,cur)

    def exeUpdate(self,cur,sql): #更新语句，可执行update,insert语句
        sta=cur.execute(sql)
        return(sta)

    def exeDelete(self,cur,*IDs): #删除语句，可批量删除 
        for eachID in IDs:
            sta=cur.execute('delete from users where id=%d'% int(eachID))
            return (sta)

    def exeQuery(self,cur,sql):  #查询语句 
        cur.execute(sql)
        return (cur)

    def connClose(self,conn,cur):    #关闭所有连接 
        cur.close()
        conn.close()
