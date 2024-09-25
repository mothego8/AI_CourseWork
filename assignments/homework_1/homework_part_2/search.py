#search

from . import state
from . import frontier
import time

def search(n):
    toc= time.time()
    s=state.create(n)
    # print(s)
    f=frontier.create(s)
    while not frontier.is_empty(f):
        s=frontier.remove(f)
        if state.is_target(s):
            tic = time.time()
            time1 = 1000*(tic-toc)
            return [s, state.path_len(s), f[1], f[2], time1]
        ns=state.get_next(s)
        for i in ns:
            frontier.insert(f,i)
        temp = time.time()
        if((temp-toc) > 5):
            time1 = 1000 * 100
            return [s, 20, 10000, 10000, time1]
    return 0

# print (search(3))





