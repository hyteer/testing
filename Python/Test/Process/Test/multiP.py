from multiprocessing import Process
import os
import time

def info(title):
    print title
    print 'module name:', __name__
    if hasattr(os, 'getppid'):  # only available on Unix
        print 'parent process:', os.getppid()
    print 'process id:', os.getpid()

def f(name):
    info('function f')
    print 'hello', name
flag = ''
if __name__ == '__main__':

    while flag != 'exit':
        info('main line')
        p = Process(target=f, args=('bob',))
        p.start()
        p.join()
        time.sleep(0.3)
        flag = raw_input('Input>')
