# just use set, because the array is strictly increasing
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        s = set(nums)
        c = 0
        for n in nums:
            if n + diff in s and n + 2 * diff in s:
                c += 1
            if n + 2 * diff >= nums[-1]:
                break
        return c