# just check distance between each pair of 1
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        d = k
        for n in nums:
            if n:
                if d < k:
                    return False
                d = 0
            else:
                d += 1
        return True