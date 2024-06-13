#1. binary search obviously
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

def firstBadVersion(n: int) -> int:
    l = 1
    r = n
    m = (l + r) // 2
    f = 0
    while l <= r:
        if isBadVersion(m):
            r = m - 1
            f = m
        else:
            l = m + 1
        m = (l + r) // 2
    return f