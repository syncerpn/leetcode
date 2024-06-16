#1. simple conditional counting
def solve(nums: list) -> int:
    c = 0
    c_max = 0
    for n in nums:
        if n:
            c += 1
            if c_max < c:
                c_max = c
        else:
            c = 0
    
    return c_max