# coding: utf-8

import csv
import codecs,chardet
import json

file = "D:\\Res\\temp\\test1.xlsx"
file2 = "D:\\Res\\temp\\smashegg_add.csv"
file3 = "D:\\Res\\temp\\testfile1_cn.csv"
file4 = "D:\\Res\\temp\\smashegg_tab.csv"

def read_csv(fileName,splitsymbol='\t',keyIndex=0,valueIndex=1):
    dataDict = {}
    with codecs.open(fileName) as csvfile:
        dataLine = csvfile.readline().strip("\n")
        print dataLine
        print chardet.detect(dataLine)
        while dataLine != "":
            tmpList = dataLine.split(splitsymbol)
            print("key:%s,value:%s" % ([tmpList[keyIndex]], tmpList[valueIndex]))
            dataDict[tmpList[keyIndex]] = tmpList[valueIndex]
            dataLine = csvfile.readline().strip("\n")
        csvfile.close()
    return dataDict

dict = read_csv(file4)
jsonstr = json.dumps(dict,encoding='utf-8')
print dict
print jsonstr

