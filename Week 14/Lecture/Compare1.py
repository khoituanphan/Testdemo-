import numpy
import time
def trad():
    t1 = time.time
    x = range(100000000)
    y = range(100000000)
    z = []
    for i in range (len(x)):
        z.append (x[i] + y[i])
    return time.time() -t1
trad()
