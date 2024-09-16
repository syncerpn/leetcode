# fairly easy with hash set
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        v = set()
        ans = []
        for n in nums:
            if n in v:
                ans.append(n)
            v.add(n)
        return ans