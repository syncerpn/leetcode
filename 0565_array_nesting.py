# traversal
# no need to use set
# just boolean array
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        n = len(nums)
        ans = [-1] * n
        v = [False] * n
        for i in range(n):
            if v[i]:
                continue
            a = i
            c = 0
            while not v[a]:
                v[a] = True
                c += 1
                a = nums[a]
            ans[i] = c
        return max(ans)