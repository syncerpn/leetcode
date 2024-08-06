# prefix sum
# register or deregister after each query
class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        p = 0
        for n in nums:
            if n % 2 == 0:
                p += n
        
        ans = []
        for v, i in queries:
            n = nums[i]
            if (n + v) % 2 == 0:
                if n % 2 == 0:
                    p += v
                else:
                    p += nums[i] + v
            else:
                if n % 2 == 0:
                    p -= n
            
            nums[i] += v
            ans.append(p)
        return ans