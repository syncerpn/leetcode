# easy, after thinking for a while
class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        nums = set(nums)
        for a, b in zip(moveFrom, moveTo):
            nums.discard(a)
            nums.add(b)
        return sorted(list(nums))