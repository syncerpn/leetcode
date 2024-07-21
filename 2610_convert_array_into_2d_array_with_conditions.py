# use set
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for n in nums:
            for s in ans:
                if n not in s:
                    s.add(n)
                    break
            else:
                ans.append(set([n]))
        
        return ans