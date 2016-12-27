# coding: utf-8
import imaplib
import email,re

def my_unicode(s, encoding):
    if encoding:
        return unicode(s, encoding)
    else:
        return unicode(s)

conn=imaplib.IMAP4_SSL('imap.qq.com')
conn.login('snsshoptest@qq.com','untleuhfhsyrdaei')
print conn.list()

result, message =conn.select('INBOX')
print result, message
#conn.select("INBOX")
#conn.logout()
typeq, data = conn.search(None, 'ALL')
print data

msgList = data[0].split()
num = len(msgList)
print "total mail: %d" % num
last = msgList[len(msgList) - 3]
print last

type,data=conn.fetch(msgList[len(msgList)-3],'(RFC822)')
msg=email.message_from_string(data[0][1])
content=msg.get_payload(decode=True)
print msg
subject = email.Header.decode_header(msg["Subject"])
sub = my_unicode(subject[0][0], subject[0][1])
strsub = 'Subject : ' + sub
print strsub

umsg = unicode(str(msg),'utf8')

reg = u"(?<=\u8d26\u53f7\uff1a)\d+"
reg_pwd = u"(?<=\u5bc6\u7801\uff1a).*(?=mch_id)"

print "From:%s" % msg["From"]
print "Date:%s" % msg["Date"]
#find = re.findall(r'(?<=账号：).*', msg)
res_id = re.findall(reg,umsg)
res_pwd = re.findall(reg_pwd,umsg)
#print match[0]
print "mch_id:%s\npassword:%s" % (res_id[0],res_pwd[0])

