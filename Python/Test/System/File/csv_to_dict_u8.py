# coding: utf-8
# 功能：从csv文件中读取一个字典
# 输入：文件名称，keyIndex,valueIndex
import json
import chardet
import codecs

file = "D:\\Res\\temp\\test1.xlsx"
file2 = "D:\\Res\\temp\\smashegg_add.csv"
file3 = "D:\\Res\\temp\\testfile1_cn.csv"
splitsymbol = ','

def readDictCSV(fileName, keyIndex=0, valueIndex=1):
    dataDict = {}
    with codecs.open(fileName,"w","utf-8") as csvFile:
        dataLine = csvFile.readline().strip("\n")
        print chardet.detect(dataLine)
        while dataLine != "":
            tmpList = dataLine.split(splitsymbol)
            dataDict[tmpList[keyIndex]] = tmpList[valueIndex]
            dataLine = csvFile.readline().strip("\n")
        csvFile.close()
    return dataDict

data = readDictCSV(file3)

print data

jsonfile = json.dumps(data, encoding='utf-8')
print jsonfile

