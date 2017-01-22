import csv

filename = 'd:\\Res\\csv\\testfile.csv'

data = []

def unicode_csv_reader(utf8_data, dialect=csv.excel, **kwargs):
    csv_reader = csv.reader(utf8_data, dialect=dialect, **kwargs)
    for row in csv_reader:
        #yield [unicode(cell, 'utf-8') for cell in row]
        templist = []
        for item in row:
            item = item.decode('utf-8')
            print "Item:",item
            templist.append(item)
        print "Templist:",templist
        data.append(templist)
    print "Data:",data
    return data



reader = unicode_csv_reader(open(filename))

'''
for field1, field2, field3 in reader:
  print field1, field2, field3
'''

def read_data():
    for item in data:
        print "Name:%s, Age:%s, Phone:%s" % (item[0],item[1],item[2])

read_data()

#print "Reader:",reader
