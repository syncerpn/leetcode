# binary search obviously
# O(logn)
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l = 0
        r = len(arr)
        while l < r:
            m = (l + r) // 2
            if arr[m] - m <= k:
                l = m + 1
            else:
                r = m
        
        return r + k