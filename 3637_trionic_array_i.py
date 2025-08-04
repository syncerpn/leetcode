# state machine if else
class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        st = -1
        for a, b in pairwise(nums):
            if b == a:
                return False
            if st == -1:
                if b < a:
                    return False
                st = 0
            elif st == 0:
                if b < a:
                    st = 1
            elif st == 1:
                if b > a:
                    st = 2
            elif st == 2:
                if b < a:
                    return False
        return st == 2