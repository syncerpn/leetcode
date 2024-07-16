# manual or this
# string converter
class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        return sum([[int(c) for c in str(n)] for n in nums], [])