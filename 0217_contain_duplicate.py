#1. pure dict count
def solve(nums: list) -> bool:
    d = {}
    for n in nums:
        if n in d:
            return True
        d[n] = 1
    
    return False