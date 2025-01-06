# not that easy actually
# may use brute force, but this solution is pure based on math
# with the given constraints: 1 <= value <= 10
class Solution:
    def maxLength(self, nums: List[int]) -> int:
        def is_valid(d):
            for a in range(2, 11):
                if d[a] > 1:
                    return False
            if sum(d[a] for a in [2, 4, 6, 8, 10]) > 1:
                return False
            if sum(d[a] for a in [3, 6, 9]) > 1:
                return False
            if sum(d[a] for a in [5, 10]) > 1:
                return False
            return True

        d = {a: 0 for a in range(1, 11)}
        l, ans = 0, 2
        for r, a in enumerate(nums):
            d[a] += 1
            while r - l > 1 and not is_valid(d):
                d[nums[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans