# coding: utf-8

import csv

csvfile = file('d:\Res\csv_test.csv', 'rb')
reader = csv.reader(csvfile)

for line in reader:
    print str(line).decode('string_escape')

csvfile.close()
