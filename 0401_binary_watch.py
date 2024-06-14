#1. obviously bin count should be cleaner; but i assume we have to do it manually
def solve(turnedOn: int) -> list:
    #from #0338 bitcounting prob:
    r = [0]
    k = 0
    for i in range(1, 60):
        if i & (i-1) == 0:
            k = 0
        r.append(1 + r[k])
        k += 1
    
    m = {}
    h = {}
    for i, n in enumerate(r):
        if n not in m:
            m[n] = []
        m[n].append(i)
        if i >= 12:
            continue

        if n not in h:
            h[n] = []
        h[n].append(i)

    time = []
    for i in range(turnedOn+1):
        if i not in h or turnedOn-i not in m:
            continue
        for hi in h[i]:
            for mi in m[turnedOn-i]:
                time.append(f"{hi}:{mi:02}")
    return time