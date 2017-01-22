# coding: utf-8

import csv
import codecs

csvfile = file('d:\Res\csv_test_u8.csv', 'wb')
csvfile.write(codecs.BOM_UTF8)
writer = csv.writer(csvfile)
writer.writerow(['姓名', '年龄', '电话'])

data = [
    ('小河', '25', '1234567'),
    ('小芳', '18', '789456')
]
writer.writerows(data)

csvfile.close()