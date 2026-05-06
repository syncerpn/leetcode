# prefix max and min
class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        l, L = -inf, []
        r, R =  inf, []
        n = len(nums)
        for i in range(n):
            l = max(l, nums[i])
            L.append(l)
            r = min(r, nums[~i])
            R.append(r)
        
        for i in range(n-1):
            if L[i] <= R[n-2-i]:
                return i+1
        return 0

# or just make it more beautiful
class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        left = 0
        global_max = nums[0]
        max_left = nums[left]
        for i in range(1, len(nums)):
            if nums[i] > global_max:
                global_max = nums[i]
            if nums[i] < max_left:
                left = i
                max_left = global_max
        return left + 1