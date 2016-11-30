# encoding: utf-8
import re

str = '<xml><retcode>12001</retcode><retmsg>第三方订单号已存在!</retmsg></xml>'

match = re.match(r"<xml>",str)

if match is not None:
	print 'match success, position:',match.span()
else:
	print 'match result is None.'

