f = { }
f[4] = 1
f[3] = 2
f[6] = 3
f[5] = 4
f[2] = 5
f[1] = 6

g = { }
g[3] = 1
g[6] = 2
g[5] = 3
g[2] = 4
g[1] = 5
g[4] = 6

nuts = [[1,2,3,4,5,6],
            [1,4,3,6,5,2],
            [1,4,6,2,3,5],
            [1,6,2,4,5,3],
            [1,6,4,2,5,3],
            [1,6,5,3,2,4],
            [1,6,5,4,3,2]]

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

nuts1 =sorted( [standard([f[n] for n in nut]) for nut in nuts])
nuts2= sorted([standard([g[n] for n in nut] )for nut in nuts])

print(nuts1)
print(nuts2)
