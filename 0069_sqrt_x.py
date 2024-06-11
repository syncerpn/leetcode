#1. binary search
def solve(x: int) -> int:
    if x < 2:
        return x
    
    l = 2
    r = x // 2
    m = (l + r) // 2
    while l <= r:
        if m * m == x:
            return m
        elif m * m < x:
            l = m + 1
        else:
            r = m - 1
        
        m = (l + r) // 2
    
    return m