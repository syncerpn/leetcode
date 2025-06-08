# two pass O(n)
# is there any one pass solution?
class Solution:
    def canMakeEqual(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        for t in [-1, 1]:
            p, a = 0, nums[0]
            for i in range(1, n):
                b = nums[i]
                if a == t:
                    p += 1
                    b = -b
                a = b
            
            if a == -t and p <= k:
                return True
        return False

# likely one pass
class Solution:
    def canMakeEqual(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        p, q, a, b = 0, 0, nums[0], nums[0]
        for i in range(1, n):
            if a == 1:
                a = -nums[i]
                p += 1
            else:
                a = nums[i]
            
            if b == -1:
                b = -nums[i]
                q += 1
            else:
                b = nums[i]
        
        return (a == -1 and p <= k) or (b == 1 and q <= k)