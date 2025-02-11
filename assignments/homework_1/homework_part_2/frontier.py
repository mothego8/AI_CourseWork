'''
implements a priority queue using a minimum heap
the heap is represented by a list
the parent of index i is in index (i-1)//2
the left child of index i is in index 2i+1
the right side of index i is in index 2i+2
'''
from . import state

#implements a priority queue
#[list of states, total num of states]

one = False
two = False
three = False

def create(s):
    return [[s], 1, 0, state.path_len(s)]

def is_empty(f):
    return f==[]    # returns true iff f is empty list
def insert(h, s):
    #inserts state s to the frontier
    f=h[0]
    h[1]+=1
    f.append(s)     # inserts the new state as the last item
    i=len(f)-1      # i gets its value
    # move the item with smallest value to the root
    while i>0 and val(f[i])<val(f[(i-1)//2]): # while item i's value is smaller than the value of his father, swap!
        # the next three lines swap i and his father
        t=f[i]
        f[i]=f[(i-1)//2]
        f[(i-1)//2]=t
        i=(i-1)//2  # i moves upwards

def remove(h):
    if is_empty(h):
        return 0
    f=h[0]
    s=f[0]
    h[2] += 1
    f[0]=f[len(f)-1]    # the last leaf becomes the root
    del f[-1]       # delete the last leaf
    heapify(f,0)    # fixing the heap
    return s

def val(s):  # returns f(x) which is path len + heuristic distance from target
    if one:
        return state.hdistance(s)+state.path_len(s)
    elif two:
        return state.hdistance1(s)+state.path_len(s)
    else:
        return state.hdistance2(s)+state.path_len(s)
    
'''
for greedy best first search val returns hdistance
for uniform cost val returns path len
'''

def heapify(f,i):   # fix the heap by rolling down from index i
    # compares f[i] with its children
    # if f[i] is bigger than at least one of its children
    # f[i] and its smallest child are swapped
    minSon=i    # define i as minSon
    if 2*i+1<len(f) and val(f[2*i+1])<val(f[minSon]):   # if f[i] has a left son
                                        # and its left son is smaller than f[i]
        minSon=2*i+1                    # define the left son as minSon
    if 2*i+2<len(f) and val(f[2*i+2])<val(f[minSon]):   # if f[i] has a right son
                                        # and its right son is smaller than f[minSon]
        minSon=2*i+2                    # define the right son as minSon
    if minSon!=i:                       # if f[i] is bigger than one of its sons
        t=f[minSon]                     # swap f[i] with the smaller son
        f[minSon]=f[i]
        f[i]=t
        heapify(f, minSon)              # repeat recursively

        

        

    

