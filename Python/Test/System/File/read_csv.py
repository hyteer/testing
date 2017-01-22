# coding: utf-8
import sys
import csv

print "args:",len(sys.argv)

csvfile = file('d:\Res\csv_test.csv', 'rb')
reader = csv.reader(csvfile)
data = []

for line in reader:
    line_data = str(line).decode('string_escape')
    print str(line).decode('string_escape')
    data.append(line_data)

csvfile.close()

print "Data: ",data
for item in data:
    print "item:",item

