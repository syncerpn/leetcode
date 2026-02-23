# basically it is just dp with memoi or backtrack
# why made it complicated?
class Solution:
    def countSequences(self, nums: List[int], k: int) -> int:
        dp = {}
        E = {1: (0, 0, 0), 2: (1, 0, 0), 3: (0, 1, 0), 4: (2, 0, 0), 5: (0, 0, 1), 6: (1, 1, 0)}
        def backtrack(i, e2, e3, e5):
            if i == len(nums):
                if e2 >= 0 and e3 >= 0 and e5 >= 0 and (2 ** e2) * (3 ** e3) * (5 ** e5) == k:
                    return 1
                return 0

            if (i, e2, e3, e5) in dp:
                return dp[(i, e2, e3, e5)]
            
            a = nums[i]
            ans  = backtrack(i+1, e2, e3, e5)
            ans += backtrack(i+1, e2 + E[a][0], e3 + E[a][1], e5 + E[a][2])
            ans += backtrack(i+1, e2 - E[a][0], e3 - E[a][1], e5 - E[a][2])
            dp[(i, e2, e3, e5)] = ans
            return ans
        
        return backtrack(0, 0, 0, 0)
            