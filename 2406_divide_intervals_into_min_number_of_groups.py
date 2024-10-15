# sort, heap, and greedy
class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        h = []
        for l, r in intervals:
            if h:
                rmin = heapq.heappop(h)
                if rmin >= l:
                    heapq.heappush(h, rmin)
            heapq.heappush(h, r)
        return len(h)

# line sweep with 1 on start and -1 on end
class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        A = []
        for l, r in intervals:
            A.append([l, 1])
            A.append([r + 1, -1])
        ans = s = 0
        for a, d in sorted(A):
            s += d
            ans = max(ans, s)
        return ans

# prefix sum with big mem
class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        CONSTRAINT_MAX = 10 ** 6 + 2
        A = [0] * CONSTRAINT_MAX
        for l, r in intervals:
            A[l] += 1
            A[r+1] -= 1
        
        s = ans = 0
        for a in A:
            s += a
            ans = max(ans, s)

        return ans

# prefix sum with big mem with limited searching range
class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        CONSTRAINT_MAX = 10 ** 6 + 2
        A = [0] * CONSTRAINT_MAX
        l_min = CONSTRAINT_MAX
        r_max = 0
        for l, r in intervals:
            A[l] += 1
            A[r+1] -= 1
            l_min = min(l_min, l)
            r_max = max(r_max, r+2)
        
        s = ans = 0
        for i in range(l_min, r_max):
            s += A[i]
            ans = max(ans, s)

        return ans