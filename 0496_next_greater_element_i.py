#1. use set and hashmap for quick lookup, updating result as it goes
def solve(nums1: list, nums2: list) -> list:
    d = {}
    res = []
    for i, n in enumerate(nums1):
        d[n] = i
        res.append(-1)
    
    s = set()
    for n in nums2:
        to_be_removed = []
        for k in s:
            if k < n:
                res[d[k]] = n
                to_be_removed.append(k)
        for k in to_be_removed:
            s.remove(k)
        if n in d:
            s.add(n)
    
    return res

#1. monostack: a new data structure to learn
#2. using stack s as monostack, map m to track next greater for each num in nums2
#3. then just query nums1 with m to find out the result
def solve2(nums1: list, nums2: list) -> list:
    s = []
    m = {}
    r = []

    for n in nums2:
        while s and s[-1] < n:
            k = s.pop()
            m[k] = n
        s.append(n)
    
    while s:
        k = s.pop()
        m[k] = -1
    
    for n in nums1:
        r.append(m[n])

    return r