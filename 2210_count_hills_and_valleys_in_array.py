# is it going up or down?
class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        go_up = None
        c = 0
        for a, b in pairwise(nums):
            if go_up is None:
                if b > a:
                    go_up = True
                elif b < a:
                    go_up = False
            else:
                if b > a and not go_up:
                    c += 1
                    go_up = True
                elif b < a and go_up:
                    c += 1
                    go_up = False
        return c