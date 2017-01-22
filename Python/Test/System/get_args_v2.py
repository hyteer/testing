# coding: utf-8
import sys
import csv
import json

print "args:",len(sys.argv)

filename = 'd:\\Res\\csv\\wkd_test.csv'
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

def read_data():
    for item in data:
        print "Name:%s, Url:%s" % (item[0],item[1])

read_data()