# sum
# hashmap
# and for each number, check the remaining sum and whether half of it exists in the array
class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        d = Counter(nums)
        s = sum(nums)
        ans = None
        for n in nums:
            t = (s - n) // 2
            if t * 2 == s - n and t in d:
                if t != n or d[t] > 1:
                    if ans is None or ans < n:
                        ans = n
        return ans