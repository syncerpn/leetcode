#1. count and append
def solve(nums1: list, nums2: list) -> list:
    d = {}
    r = []
    for n in nums1:
        if n not in d:
            d[n] = 0
        d[n] += 1
    
    for n in nums2:
        if n not in d:
            continue

        if d[n] <= 0:
            continue
        
        r.append(n)
        d[n] -= 1

    return r