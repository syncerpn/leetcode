# used of itertools.cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def cmp(x, y):
            if x + y > y + x:
                return 1
            elif x + y < y + x:
                return -1
            return 0
        nums = [str(n) for n in nums]
        nums.sort(reverse=True, key=cmp_to_key(cmp))
        ans = "".join(nums).lstrip("0")
        return ans if ans else "0"