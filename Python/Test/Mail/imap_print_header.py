import imaplib, string, email
M = imaplib.IMAP4_SSL("imap.qq.com")
print M
#try:
try:
    M.login('snsshoptest@qq.com','untleuhfhsyrdaei')
except Exception,e:
    print 'login error: %s' % e
    M.close()
M.select()
result, message = M.select()
typ, data = M.search(None, 'ALL')
print len(string.split(data[0]))


"""
    for num in string.split(data[0]):
        try:
            typ, data = M.fetch(num, '(RFC822)')
            msg = email.message_from_string(data[0][1])
            print msg["From"]
            print msg["Subject"]
            print msg["Date"]
            print "_______________________________"
        except Exception,e:
            print 'got msg error: %s' % e
            M.logout()
            M.close()
except Exception, e:
    print 'imap error: %s' % e
    M.close()
"""