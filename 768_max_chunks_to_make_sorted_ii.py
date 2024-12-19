# sorting solution O(nlogn)
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        indices = list(range(len(arr)))
        sarr = sorted(indices, key=lambda i: arr[i])
        m, ans = 0, 0
        for i, n in enumerate(sarr):
            m = max(m, n)
            if m == i:
                ans += 1
        return ans

# how about an O(n) solution with monostack
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        s = []
        for a in arr:
            m = a
            while s and s[-1] > a:
                m = max(m, s.pop())
            
            s.append(m)
        return len(s)