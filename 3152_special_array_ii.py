# fairly easy/straightforward with prefix sum/encoded array
class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        s = [0]
        for a, b in pairwise(nums):
            if a % 2 == b % 2:
                s.append(0)
            else:
                s.append(s[-1] + 1)
        ans = []
        for l, r in queries:
            if r - l == s[r] - s[l]:
                ans.append(True)
            else:
                ans.append(False)
        return ans