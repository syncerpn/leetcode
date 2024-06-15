#1. binary search should be fastest; else you can do iterative accumulation
def solve(n: int) -> int:
    l = 0
    r = n
    m = (l + r) // 2
    while l <= r:
        if n == m * (m + 1) // 2:
            return m
        elif n > m * (m + 1) // 2:
            l = m + 1
        else:
            r = m - 1
        m = (l + r) // 2
        
    return m