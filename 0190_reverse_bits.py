#1. would you prefer string manip?
def solve(n: int) -> int:
    s = bin(n)[2:]
    s = s[::-1] + "0" * (32-len(s))
    return int(s, 2)

#1. or bit manip?
def solve2(n: int) -> int:
    r = 0
    for _ in range(31):
        if n & 1:
            r = r | 1
        
        n = n >> 1
        r = r << 1
    
    return r | 1 if n & 1 else r
