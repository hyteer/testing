#!/usr/bin/python
# -*- coding: UTF-8 -*-

import thread
import time

# 为线程定义一个函数
def print_time( threadName, delay):
   count = 0
   while count < 3:
      time.sleep(delay)
      count += 1
      print "%s: %s" % ( threadName, time.ctime(time.time()) )

def print_test( name, str,delay):
    time.sleep(delay)
    print "%s Content: %s"%(name, str)

# 创建两个线程
def multi():
    flag = ''
    while flag != 'exit':
        print "Please input:"
        flag = raw_input('>')
        print "Test will go on..."


i=0

try:
   #thread.start_new_thread( print_time, ("Thread-1", 1, ) )
   thread.start_new_thread(multi())
   #thread.start_new_thread( print_test,("[Thread-A]", "Tony",2))
   #thread.start_new_thread( print_test,("[Thread-B]", "Dyci",1))
   #thread.start_new_thread( print_time, ("Thread-2", 0.9, ) )
except:
   print "Error: unable to start thread"


while 1:
   pass
