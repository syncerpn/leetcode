#1. binary search should do
def solve(num: int) -> bool:
    if num == 1:
        return True
    l = 1
    r = num // 2
    m = (l + r) // 2
    while l <= r:
        if m * m == num:
            return True
        elif m * m < num:
            l = m + 1
        else:
            r = m - 1
        m = (l + r) // 2
    
    return m * m == num