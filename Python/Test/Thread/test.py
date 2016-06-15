#-*- encoding: gb2312 -*-
import threadingDemo
import time

class Test(threadingDemo.Thread):
    def __init__(self, num):
        threadingDemo.Thread.__init__(self)
        self._run_num = num

    def run(self):
        global count, mutex
        threadname = threadingDemo.currentThread().getName()

        for x in xrange(0, int(self._run_num)):
            mutex.acquire()
            count = count + 1
            mutex.release()
            print threadname, x, count
            time.sleep(1)

if __name__ == '__main__':
    global count, mutex
    threads = []
    num = 4
    count = 1
    # 创建锁
    mutex = threadingDemo.Lock()
    # 创建线程对象
    for x in xrange(0, num):
        threads.append(Test(10))
    # 启动线程
    for t in threads:
        t.start()
    # 等待子线程结束
    for t in threads:
        t.join()