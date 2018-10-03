import datetime
from functools import lru_cache
#from random import shuffle

x = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]
upper_limit = 100
desired_score = 96

def printx(x):
    '''Print 2-dimentional list x'''
    for line in x:
        print('{0:02d} {1:02d} {2:02d} {3:02d} {4:02d} {5:02d} {6:02d} {7:02d} {8:02d} {9:02d}'.format(*line))

@lru_cache(maxsize=100)
def moves2go(i, j):
    #moves = [(-2,+1), (-1,+2), (+1,+2), (+2,+1), (+2,-1), (+1,-2), (-1,-2), (-2,-1)]
    moves = [(+1,+2), (+2,+1), (+2,-1), (-1,+2), (-2,+1), (-2,-1), (+1,-2), (-1,-2)]
    #shuffle(moves) # randomize attempted moves
    return [(i+v, j+h) for v, h in moves if 0 <= i+v <= 9 and 0 <= j+h <= 9]

def go(i, j, n, x):
    x[i][j] = n
    global desired_score
    global upper_limit
    if n >= desired_score:
        print('# {0:s} Scored {1:d} '.format(str(datetime.datetime.now()), n))
        print('#', moves2go.cache_info())
        printx(x)
        if n == upper_limit:
            return n
        else:
            desired_score += 1
    for v, h in ((v, h) for v, h in moves2go(i, j) if x[v][h] == 0):
        score = go(v, h, n+1, x)
        if score >= desired_score:
            return score
    x[i][j] = 0
    return n-1


for i in [2]: #reversed(range(5)):
    for j in [0]: #reversed(range(i, 5)):
        print('# {0:s} Started at {1:d}, {2:d}'.format(str(datetime.datetime.now()), i, j))
        score = go(i, j, 1, x)
        if score >= upper_limit:
            break
    if score >= upper_limit:
        print('# {0:s} Done'.format(str(datetime.datetime.now())))
        break
else:
    print('# {0:s} Desired score {1:d} was not reached'.format(str(datetime.datetime.now()), desired_score))
