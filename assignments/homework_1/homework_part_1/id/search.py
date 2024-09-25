#search

from . import state
from . import frontier
import time


def search(n):
    tic = time.time()
    s=state.create(n)
    #print(s)
    f=frontier.create(s)
    while not frontier.is_empty(f):
        s=frontier.remove(f)
        if state.is_target(s):
            toc = time.time()
            time1= 1000*(toc-tic)
            return [s, f[1], f[4], f[5], round(time1, 2)]
        ns=state.get_next(s)
        #print(ns)
        for i in ns:
            frontier.insert(f,i)
        temp = time.time()
        if((temp-tic) > 5):
            time1 = 1000 * 100
            return [s, 20, 10000, 10000, time1]
    return 0
