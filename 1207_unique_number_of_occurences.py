def solve(arr: list) -> bool:
    d = {}
    for n in arr:
        if n not in d:
            d[n] = 0
        d[n] += 1
    
    f = {}
    for n in d:
        if d[n] not in f:
            f[d[n]] = 0
        else:
            return False
    
    return True