#driveYaNuts.py
from itertools import permutations
from random import sample
'''
Call the center nut "nut 0", the north nut "nut 1" and number
the remaining nuts clockwise from 1 to 6.  Likewise call the
north side of each nut "side 1", and number the other sides
clockwise from 2 to 6.  

'''
nuts = [(1,)+p for p in permutations(range(2,7), 5)]
constraints = { }

'''
if (b,c,d) is in constraints[a] it means that side b of nut a
must match side d of nut c

There are 12 constraints, one for each edge of nut zero,
and one for each edge lying on two of the outer 6 nuts.
'''

constraints[1] = [(4,0,1)]
constraints[2] = [(5,02),(6,1,3)]
constraints[3] = [(6,0,3),(1,2,4)]
constraints[4] = [(1,0,4), (2,3,5)]
constraints[5] = [(2,0,5),(1,6,4)]
constraints[6] = [(3,0,6), (4,5,1), (2,1,5)]

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
    return rotate(nut,6-i)

def solutions(nutSet):
    '''
    Return all solutions to drive ya nuts with the given set of 7 nuts
    '''
    solns = []
    available = { } # nuts available for use at this position
    used = { }       # nuts placed at positions prior to this one
    nuts = { }
    position = 0
    available[position] = nutSet
    used[position] = set()
    while position >= 0:
        while available[position]:
            nut = available.pop()
            rule = constraints[position][0]
            match = nuts[0][rule[2]]
            now = 1+ nut.index(match)
            move = rule[0] - now
            if move < 0: move += 6
            nuts[position] = rotate(nut, move)
            if position == 6:
                solutions.append(nuts[:])
            position += 1
            used[position] = used[position-1]  | {nut}
            available[position] = [ ]
            for nut in nutset:
                if nut in used[position]:
                    continue
                
            
            
            
           
            
            
            
    
    
