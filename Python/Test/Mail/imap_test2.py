# coding: utf-8
import imaplib
import email,re
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

"""
type,data=conn.fetch(msgList[len(msgList)-3],'(RFC822)')
msg=email.message_from_string(data[0][1])
content=msg.get_payload(decode=True)
"""

if num > 3:
    count = 3
i= 1
while i <= count:
    type,data=conn.fetch(msgList[num-i],'(RFC822)')
    msg=email.message_from_string(data[0][1])
    content=msg.get_payload(decode=True)
    print u"第%d封" % i
    print msg
    print "From:%s" % msg["From"]
    subject = email.Header.decode_header(msg['Subject'])
    #print "Subject:%s" % msg["Subject"]
    print "Subject:%s" % subject
    print "Date:%s" % msg["Date"]

    i += 1



"""
# Get mail match info
umsg = unicode(str(msg),'utf8')

reg = u"(?<=\u8d26\u53f7\uff1a)\d+"
reg_pwd = u"(?<=\u5bc6\u7801\uff1a).*(?=mch_id)"


#find = re.findall(r'(?<=账号：).*', msg)
res_id = re.findall(reg,umsg)
res_pwd = re.findall(reg_pwd,umsg)
#print match[0]
print "mch_id:%s\npassword:%s" % (res_id[0],res_pwd[0])
"""

