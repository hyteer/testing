# coding: utf-8
import csv
# 功能：将一个二重列表写入到csv文件中
# 输入：文件名称，数据列表
file = "D:\\Res\\temp\\testfile1.csv"
file2 = "D:\\Res\\temp\\smashegg_add.csv"

def createListCSV(fileName, dataList=[]):
    with open(fileName, "wb") as csvFile:
        csvWriter = csv.writer(csvFile)
        for data in dataList:
            csvWriter.writerow(data)
        csvFile.close


# 功能：从文本文件中读取返回为列表的形式
# 输入：文件名称，分隔符（默认,）
def readListCSV(fileName, splitsymbol=","):
    dataList = []
    with open(fileName, "r") as csvFile:
        dataLine = csvFile.readline().strip("\n")
        while dataLine != "":
            tmpList = dataLine.split(splitsymbol)
            dataList.append(tmpList)
            dataLine = csvFile.readline().strip("\n")
        csvFile.close()
    return dataList

#createListCSV(dataList=['aa','bb','cc'])

#print readListCSV(file2)
