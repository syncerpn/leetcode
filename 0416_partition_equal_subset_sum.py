# solved with O(n*s)
# and bitmask
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2:
            return False
        
        s //= 2
        dp = [False] * (s + 1)
        dp[0] = True
        for n in nums:
            for i in range(s,-1,-1):
                if i+n <= s:
                    dp[i+n] |= dp[i]
        return dp[s]

# probably, set will also work
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2:
            return False
        
        s //= 2
        v = set([0])
        for n in nums:
            for i in range(s,-1,-1):
                if i in v:
                    v.add(n+i)
        return s in v

# same but extra mem
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2:
            return False
        
        s //= 2
        v = set([0])
        for n in nums:
            v_n = set()
            for i in v:
                v_n.add(n+i)
                v_n.add(i)
            v = v_n
        return s in v

# true bitmask
# super fast
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return False

        s = sum(nums)
        if s % 2:
            return False

        s //= 2
        dp = 1
        for n in nums:
            dp |= dp << n
        
        return dp & (1 << s)