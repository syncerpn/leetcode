# O(n) time, O(1) space
# build up smallest so far and middle so far
# key thing is smallest does not necessarily appear before middle
# but having middle implies that there must be a smaller-than-middle before it
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        CONSTRAINTS_MAX = 1 << 32 - 1
        l = m = CONSTRAINTS_MAX
        for n in nums:
            if n <= l:
                l = n
            elif n <= m:
                m = n
            else:
                return True
        return False

# we can use mono stack, but too slow and space hungry, not optimal