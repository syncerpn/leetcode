# python makes it beautifully done
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        nums[0::2], nums[1::2] = nums[:n], nums[n:]
        return nums