#1. recursive + mem
cache = {0: 0, 1: 1}
def solve(n: int) -> int:
    if n < 2:
        return n
    if n in cache:
        return cache[n]
    
    r = solve(n-1) + solve(n-2)
    cache[n] = r
    return r