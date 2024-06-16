#1. similar to #0496, monostack is just beautiful
def solve(nums: list) -> list:
    s = []
    r = [-1 for _ in nums]
    i = 0
    l = len(nums)
    while True:
        n = nums[i]
        while s and nums[s[-1]] < n:
            j = s.pop()
            r[j] = n
        if s and i == s[0]:
            break
        s.append(i)
        i = (i + 1) % l
    return r