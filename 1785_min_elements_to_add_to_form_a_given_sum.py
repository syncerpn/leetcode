# easy
class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        s = sum(nums)
        d = abs(goal - s)
        return d // limit + int(d % limit != 0)