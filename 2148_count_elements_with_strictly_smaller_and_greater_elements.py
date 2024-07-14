# try to make it O(n) single pass
class Solution:
    def countElements(self, nums: List[int]) -> int:
        c_max = 0
        c_min = 0
        n_max = max(nums[:2])
        n_min = min(nums[:2])
        for n in nums:
            if n > n_max:
                n_max = n
                c_max = 1
            elif n == n_max:
                c_max += 1
            if n < n_min:
                n_min = n
                c_min = 1
            elif n == n_min:
                c_min += 1
        
        return max(0, len(nums) - c_min - c_max)
                
