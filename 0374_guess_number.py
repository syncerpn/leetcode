#1. pure binary search
#2. be careful with implementation: l = m + 1 and r = m - 1 should be the way

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

def guessNumber(n: int) -> int:
    l = 1
    r = n
    m = l + (r - l) // 2
    while l <= r:
        g = guess(m)
        if g == 0:
            return m
        elif g > 0:
            l = m + 1
        else:
            r = m - 1

        m = l + (r - l) // 2
    
    return m