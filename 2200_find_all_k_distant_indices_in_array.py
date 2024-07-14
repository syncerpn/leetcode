# one-pass + early stop
class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        l = 0
        r = []
        for i, n in enumerate(nums):
            if n == key:
                js = max(l, i-k)
                je = min(i+k+1, len(nums))
                r += list(range(js,je))
                l = je
            if l == len(nums):
                break
        return r