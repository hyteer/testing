import time

GTIME = time.time()


def time_triger():
    global GTIME
    if GTIME <= time.time():
        GTIME += 4
        return True
    else:
        return False


while True:
    # time = time.time()
    if time_triger():
        print "Triger is active."
    else:
        print "waiting..."
    time.sleep(1)
# just a test
