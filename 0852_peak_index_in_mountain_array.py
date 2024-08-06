# binary search for O(logn)
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l = 1
        r = len(arr) - 2
        while l <= r:
            m = (l + r) // 2
            if arr[m-1] < arr[m] > arr[m+1]:
                return m
            elif arr[m] > arr[m+1]:
                r = m-1
            else:
                l = m+1
        return l

# learn new thing everyday
# for unimodality: function with only one peak
# golden-section search (for continuous domain)
# or fibonacci search (for discrete domain)
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        def gold1(l, r):
            return l + int(round((r - l) * 0.382))

        def gold2(l, r):
            return l + int(round((r - l) * 0.618))
        l, r = 0, len(arr) - 1
        x1, x2 = gold1(l, r), gold2(l, r)
        while x1 < x2:
            if arr[x1] < arr[x2]:
                l = x1
                x1 = x2
                x2 = gold1(x1, r)
            else:
                r = x2
                x2 = x1
                x1 = gold2(l, x2)
        return arr.index(max(arr[l:r + 1]), l)