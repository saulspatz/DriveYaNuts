from itertools import permutations

nuts  = [(1,)+p for p in permutations(range(2,7))]

def rotate(nut, n):
    '''
    Return nut rotated clockwise n times
    ''' 
    return nut[n:] +nut[:n]

def standard(nut):
    '''
    Return nut rotated so 1 is at the top (north) 
    '''
    if nut[0] == 1:
        return nut
    i = nut.index(1)
    return rotate(nut,i)

def sigma(n):
    return 1 if n == 6  else n+1