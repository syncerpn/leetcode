# this is okay with small constraints
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        d = {}
        ans = []
        h = []
        for i, a in enumerate(nums):
            if i >= k:
                b = nums[i-k]
                d[b] -= 1
                if d[b] == 0:
                    del d[b]
                
            if a not in d:
                d[a] = 0
            d[a] += 1
            if i >= k - 1:
                s = sorted([(d[k], k) for k in d], reverse=True)
                ans.append(sum([a * b for a, b in s[:x]]))
        return ans