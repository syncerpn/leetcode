#1. find the next greater first
#2. then try to encode it into a new format for find the next greater (second one)
#3. basically the same algorithm as the first
def solve(nums: list) -> list:
    def next_greater(nums: list) -> list:
        s = []
        r = [-1 for _ in nums]
        i = 0
        while i < len(nums):
            n = nums[i]
            while s and nums[s[-1]] < n:
                j = s.pop()
                r[j] = i
            s.append(i)
            i = i + 1
        return r

    f = sorted([(j, i) for i, j in enumerate(next_greater(nums))])
    r = [-1 for _ in nums]
    s = []
    i = 0
    j = 0
    while i < len(f):
        while j < len(f) and f[j][0] < i:
            if f[j][0] != -1:
                s.append(f[j])
            j += 1
        
        while s:
            if nums[s[-1][1]] < nums[i] and s[-1][0] < i:
                k = s.pop()
                r[k[1]] = nums[i]
                continue
            break
        
        i += 1

    return r

#1. two stack solution is also beautiful and clean
def solve2(nums: list) -> list:
    res = [-1] * len(nums)
    p = [] #decreasing stack that stores indices that already met the first greater num.
    s = [] #decreasing stack that stores indices.

    for i, num in enumerate(nums):
        #indices in p meet second greater num.
        while p and nums[p[-1]] < num:
            res[p.pop()] = num
        #push indices that meet the first greater num from s to p.
        #we need a temp array to make indices in p increasing.
        d = []
        while s and nums[s[-1]] < num:
            d.append(s.pop())
        
        p += d[::-1]
        s.append(i)

    return res