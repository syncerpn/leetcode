# need revisit
# segment tree solution
class SegTree:
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.maxv = [0] * (4 * self.n)
        self.minv = [0] * (4 * self.n)
        self.build(1, 0, self.n - 1, nums)

    def build(self, node: int, l: int, r: int, nums: List[int]):
        if l == r:
            self.maxv[node] = self.minv[node] = nums[l]
            return
        m = (l + r) // 2
        self.build(node * 2, l, m, nums)
        self.build(node * 2 + 1, m + 1, r, nums)
        self.maxv[node] = max(self.maxv[node * 2], self.maxv[node * 2 + 1])
        self.minv[node] = min(self.minv[node * 2], self.minv[node * 2 + 1])

    def queryMax(self, node: int, l: int, r: int, ql: int, qr: int) -> int:
        if ql <= l and r <= qr:
            return self.maxv[node]
        m = (l + r) // 2
        res = -(10**18)
        if ql <= m:
            res = max(res, self.queryMax(node * 2, l, m, ql, qr))
        if qr > m:
            res = max(res, self.queryMax(node * 2 + 1, m + 1, r, ql, qr))
        return res

    def queryMin(self, node: int, l: int, r: int, ql: int, qr: int) -> int:
        if ql <= l and r <= qr:
            return self.minv[node]
        m = (l + r) // 2
        res = 10**18
        if ql <= m:
            res = min(res, self.queryMin(node * 2, l, m, ql, qr))
        if qr > m:
            res = min(res, self.queryMin(node * 2 + 1, m + 1, r, ql, qr))
        return res

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        seg = SegTree(nums)
        pq = [
            (
                -(
                    seg.queryMax(1, 0, n - 1, l, n - 1)
                    - seg.queryMin(1, 0, n - 1, l, n - 1)
                ),
                l,
                n - 1,
            )
            for l in range(n)
        ]
        heapq.heapify(pq)
        ans = 0
        while k:
            negVal, l, r = heapq.heappop(pq)
            ans -= negVal
            k -= 1
            if r > l:
                heapq.heappush(
                    pq,
                    (
                        -(
                            seg.queryMax(1, 0, n - 1, l, r - 1)
                            - seg.queryMin(1, 0, n - 1, l, r - 1)
                        ),
                        l,
                        r - 1,
                    ),
                )
        return ans

# some unknown style just so fast
class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n   = len(nums)
        vis = set()

        # Sort indices by value (ascending), ties broken by index
        ids = sorted(range(n), key=lambda x: (nums[x], x))

        uid = itertools.count()   # tie-breaker for the heap

        def compute_val(i, j, l, r):
            """
            Find the max-spread pair within position window (i, j) exclusive,
            searching within ids[l..r].
            Returns (val, i, j, l, r) or None if invalid / already visited.
            """
            if (i, j) in vis:
                return None
            vis.add((i, j))

            # Advance l until ids[l] is strictly inside (i, j)
            while l < n and (ids[l] <= i or ids[l] >= j):
                l += 1
            # Retreat r until ids[r] is strictly inside (i, j)
            while r >= 0 and (ids[r] <= i or ids[r] >= j):
                r -= 1

            if l > r:
                return None

            val = nums[ids[r]] - nums[ids[l]]
            return (val, i, j, l, r) if val > 0 else None

        res = 0
        pq  = []   # max-heap (negate val)

        first = compute_val(-1, n, 0, n - 1)
        if first:
            val, i, j, l, r = first
            heapq.heappush(pq, (-val, next(uid), i, j, l, r))

        while pq and k > 0:
            neg_val, _, i, j, l, r = heapq.heappop(pq)
            val = -neg_val

            # Positions of the min-value and max-value elements
            ni = min(ids[l], ids[r])   # leftmost of the two extreme positions
            nj = max(ids[l], ids[r])   # rightmost

            # Number of (left, right) pairs with left in (i, ni] and right in [nj, j)
            cnt  = min((ni - i) * (j - nj), k)
            k   -= cnt
            res += val * cnt

            # Split into two sub-problems and push their best pairs
            for entry in [compute_val(ni, j, l, r),
                          compute_val(i, nj, l, r)]:
                if entry:
                    ev, ei, ej, el, er = entry
                    heapq.heappush(pq, (-ev, next(uid), ei, ej, el, er))

        return res