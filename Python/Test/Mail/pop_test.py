# coding: utf-8
import poplib

emailServer = poplib.POP3('pop.qq.com')
emailServer.user('snsshoptest@qq.com')
emailServer.pass_('untleuhfhsyrdaei')

# 获取一些统计信息
emailMsgNum, emailSize = emailServer.stat()
print 'email number is %d and size is %d'%(emailMsgNum, emailSize)

# 遍历邮件，并打印出每封邮件的标题
for i in range(emailMsgNum):
    for piece in emailServer.retr(i+1)[1]:
        if piece.startswith('Subject'):
            print '\t' + piece
            break

emailServer.quit()