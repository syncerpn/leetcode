# try greedy
# those with small limits first to make sure we get some values from them
class Solution:
    def maxTotal(self, value: List[int], limit: List[int]) -> int:
        lvi = sorted((l, -v, i) for i, (v, l) in enumerate(zip(value, limit)))
        q, n = deque(), 0
        ans = 0
        p = set()
        for l, v, i in lvi:
            if i in p or l <= n:
                continue
            ans -= v
            q.append(i)
            n = len(q)
            while q and limit[q[0]] <= n:
                p.add(q.popleft())
        return ans

# optimized, dont need to save the index
class Solution:
    def maxTotal(self, value: List[int], limit: List[int]) -> int:
        lvi = sorted((l, -v, i) for i, (v, l) in enumerate(zip(value, limit)))
        q, n = deque(), 0
        ans = 0
        for l, v, i in lvi:
            if l <= n:
                continue
            ans -= v
            q.append(i)
            n = len(q)
            while q and limit[q[0]] <= n:
                q.popleft()
        return ans