#search
from . import state
from . import frontier
import time

def search(n):
    tic = time.time()
    s=state.create(n)
    f=frontier.create(s)
    added = 1
    removed = 0
    while not frontier.is_empty(f):
        s=frontier.remove(f)
        removed+=1
        if state.is_target(s):
            toc = time.time()
            time1= 1000*(toc-tic)
            return [s, state.path_len(s), added, removed, time1]
        ns=state.get_next(s)
        for i in ns:
            added+=1
            frontier.insert(f,i)
        temp = time.time()
        if((temp-tic) > 5):
            time1 = 100*1000
            return [s, 20, 10000, 10000, time1]
    return 0

