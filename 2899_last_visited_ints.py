# it is easy, but the description is confusing as fuck
# here implements a "append all at once"
class Solution:
    def lastVisitedIntegers(self, nums: List[int]) -> List[int]:
        ans = []
        s = []
        k = 0
        for i, n in enumerate(nums):
            if n == -1:
                k += 1
            if i == len(nums)-1 or n != -1:
                if k > 0:
                    j = 0
                    if k > len(s):
                        j = k - len(s)
                        k = len(s)
                    ans += s[-k:][::-1] + [-1]*j
                s.append(n)
                k = 0
        
        return ans