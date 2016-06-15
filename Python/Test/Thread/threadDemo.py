# encoding: utf-8
import time
import thread
def timer(no, interval):
    cnt = 0
    while cnt<10:
        print 'Thread:(%d) Time:%s\n'%(no, time.ctime())
        time.sleep(interval)
        cnt+=1
    thread.exit_thread()


#def test(): #Use thread.start_new_thread() to create 2 new threads
try:
    thread.start_new_thread(timer, (1, 1))   # start_new_thread方法第一个参数为函数，第二个为传递给函数的参数
    thread.start_new_thread(timer, (2, 2))
except:
    print "There's an error."


while 1:
    pass

'''
if __name__=='__main__':
    test()
    '''