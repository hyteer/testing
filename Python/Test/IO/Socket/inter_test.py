import random, time

def PrintRand():
    while True:
        print(random.randint(1,9))
        time.sleep(1)
    

if __name__ == '__main__':
    print('main start')
    td = PrintRand()
    td.setDaemon(True)
    td.start()
    try:
        while td.isAlive():
            pass
    except KeyboardInterrupt:
        print('stopped by keyboard')
    print('main end')