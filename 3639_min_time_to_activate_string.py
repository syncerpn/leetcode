# sorted list for the win
# we need to a logic to count new valid substrings every time a char is turned into star
# it can be done by check the expanding left and right until there is no other star than the new one
class Solution:
    def minTime(self, s: str, order: List[int], k: int) -> int:
        n = len(s)
        q = sortedcontainers.SortedList([-1, n])
        p = 0
        for i, m in enumerate(order):
            j = q.bisect_right(m)
            p += (m - q[j-1]) * (q[j] - m)
            if p >= k:
                return i
            q.add(m)
        
        return -1
