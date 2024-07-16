# use set, update on the way
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        m = -1
        s = set()
        for n in nums:
            if -n in s:
                m = max(m, abs(n))
            s.add(n)
        return m