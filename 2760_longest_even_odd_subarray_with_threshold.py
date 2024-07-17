# looks a bit tedious
# but logic is ok
class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        l = 0
        l_max = 0
        
        for i, n in enumerate(nums + [threshold+1]):
            if l == 0:
                if n % 2 == 0 and n <= threshold:
                    l, p = 1, n
                    l_max = max(l, l_max)
            else:
                if n % 2 != p % 2 and n <= threshold:
                    l += 1
                    l_max = max(l, l_max)
                    p = n
                else:
                    l = 0
                    if n % 2 == 0 and n <= threshold:
                        l, p = 1, n
        return l_max