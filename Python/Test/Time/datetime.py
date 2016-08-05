from datetime import datetime
now = datetime.now()
year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute
second = now.second

print now
print year
print month
print day
print "%s%s%s_%s%s%s"%(year,month,day,hour,minute,second)
print 'Text on date: %s' % ( now.strftime('%A, %B %d, %Y'))
print "Now is:%s"%(now.isoformat())