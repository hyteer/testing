import time

gtime = time.time()

def time_triger():
        global gtime
        if gtime <= time.time():
            gtime += 4
            return True
        else:
            return False


while True:
    #time = time.time()
    if time_triger() == True:
        print "Triger is active."
    else:
        print "waiting..."
    time.sleep(1)



