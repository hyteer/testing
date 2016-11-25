 # encoding: utf-8
import time

epoch_str = 1479541926

timeStamp = 1381419600
timeArray = time.localtime(epoch_str)
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)

print otherStyleTime