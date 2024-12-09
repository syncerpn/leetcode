# binary search obviously
class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def is_valid(m):
            k = maxOperations
            for n in nums:
                if n > m:
                    k -= (n // m + (n % m > 0) - 1)
                    if k < 0:
                        return False
            return True
                    
        l, r = 1, max(nums)
        while l < r:
            m = (l + r) // 2
            if is_valid(m):
                r = m
            else:
                l = m + 1
        return r

# how about using lib to make it run faster: sum
class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        l, r = 1, max(nums)
        while l < r:
            m = (l + r) // 2
            if sum((n - 1) // m for n in nums) > maxOperations:
                l = m + 1
            else:
                r = m
        return r

# this is even faster, with better l and r bounds
class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        n = len(nums)
        s = sum(nums)
        g = n + maxOperations
        if g >= s: return 1

        def is_valid(m):
            return sum(math.ceil(a / m) for a in nums) <= g
        
        l = math.ceil(s / g) - 1
        r = min(max(nums), math.floor(s / maxOperations))
        
        while l < r:
            m = (l + r) // 2
            if is_valid(m):
                r = m
            else:
                l = m + 1
        return r