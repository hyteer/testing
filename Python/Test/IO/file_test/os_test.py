# encoding:utf-8
import os


BASE_DIR = os.path.dirname(__file__) #获取当前文件夹的绝对路径
print BASE_DIR
file_path = os.path.join(BASE_DIR, 'Test_Data') #获取当前文件夹内的Test_Data文件
Test_Data = open(file_path, "r") #读取文件
for line in Test_Data:
    print line
Test_Data.close() #关闭文件