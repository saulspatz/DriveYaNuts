r = range(1,7)

with open('spokes.txt', 'w') as fout:
    for a1 in r:
        if a1 in (1,2): continue
        for a2 in r:
            if a2== a1: continue
            if a2 in (2,3): continue
            for a3 in r:
                if a3==a2: continue
                if a3 in (3,4): continue
                for a4 in r:
                    if a4 == a3: continue
                    if a4 in (4,5): continue
                    for a5 in r:
                        if a5==a4: continue
                        if a5 in (5,6): continue
                        for a6 in r:
                            if a6 in (a5,a1): continue
                            if a6 in (1,6): continue
                            fout.write('%s %s %s %s %s %s\n'%(a1,a2,a3,a4,a5,a6))
