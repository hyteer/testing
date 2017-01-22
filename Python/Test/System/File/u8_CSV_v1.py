import csv

filename = 'd:\\Res\\csv\\testfile.csv'

def unicode_csv_reader(utf8_data, dialect=csv.excel, **kwargs):
    csv_reader = csv.reader(utf8_data, dialect=dialect, **kwargs)
    for row in csv_reader:
        yield [unicode(cell, 'utf-8') for cell in row]

data = []
reader = unicode_csv_reader(open(filename))
for field1, field2, field3 in reader:
  print field1, field2, field3

print "Reader:",reader
