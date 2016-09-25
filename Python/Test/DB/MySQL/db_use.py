from db_class import mydb

db = mydb()

conn,cur = db.connDB()

sql = 'select * from users'

db.exeQuery(cur,sql)
for each in cur:
    print(each[0], each[1].decode('utf-8'))

def delete(*IDs):
    sta = db.exeDelete(cur,*IDs)
    if sta == 1:
        print "delete %s, success" % str(IDs)
    else:
        print "delete %s, fail" % str(IDs)

delete(6)

conn.commit()
db.connClose(conn,cur)

