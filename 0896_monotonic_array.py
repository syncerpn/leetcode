# find direction first, then early stop if against the direction
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        d = None
        for a, b in pairwise(nums):
            if a > b:
                if d is None:
                    d = True
                elif not d:
                    return False
            elif a < b:
                if d is None:
                    d = False
                elif d:
                    return False
        
        return True

# or more compact solution (but no early stop)
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        c = [a > b for a, b in pairwise(nums) if a != b]
        return all(c) or not any(c)