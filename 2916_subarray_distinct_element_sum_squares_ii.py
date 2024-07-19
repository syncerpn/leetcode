# votrubac's solution with memoi, dp, and segment tree with lazy propagation
# a lot of new things to learn here
class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        st = [0] * 400000 # segment tree with 4 times bigger than num range [1, 10**5]
        lazy = [0] * 400000 # lazy propagation
        last = [0] * 100001 # like a hash table/bit mask to remember that last occurence of i (100001 instead of 100000 just because num range starts at 1 instead of 0)
        mod = 10 ** 9 + 7
        def query(l, r, p=1, tl=0, tr=100000):
            # query segment tree to get info
            if l > r:
                # if out range
                return 0
            if l == tl and r == tr:
                # if full-range covered
                return st[p] + (1 + tr - tl) * lazy[p] % mod

            # else, get left and right segments
            tm = (tl + tr) // 2
            return (1 + r - l) * lazy[p] + query(l, min(r, tm), p*2, tl, tm) + query(max(l, tm+1), r, p*2+1, tm+1, tr)
        
        def add(l, r, v, p=1, tl=0, tr=100000):
            # add new distinct value to segment tree
            # update to every node might be expensive, so make use of lazy propagation
            if l == tl and r == tr:
                lazy[p] += v
            elif l <= r:
                lazy[p*2] += lazy[p]
                lazy[p*2+1] += lazy[p]
                lazy[p] = 0
                tm = (tl + tr) // 2
                add(l, min(r, tm), v, p*2, tl, tm)
                add(max(l, tm+1), r, v, p*2+1, tm+1, tr)
                st[p] = query(tl, tm, p*2, tl, tm) + query(tm+1, tr, p*2+1, tm+1, tr)
        
        sum_sq = 0
        res = 0
        for i in range(len(nums)):
            l = last[nums[i]]
            s = query(l, i)
            add(l, i, 1)
            sum_sq = (sum_sq + 2 * s + (i - l) + 1) % mod
            res = (res + sum_sq) % mod
            last[nums[i]] = i+1
        
        return res

# the fastest python solution is down here
# seems like it also uses the similar techniques (with segment tree)
class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n, inds, sums, res, mod = 1<<len(nums).bit_length(), defaultdict(lambda:-1), 0, 0, 10**9+7
        cnt, acc = [0]*(2*n), [0]*(2*n)

        for i,num in enumerate(nums):
            prv, inds[num] = inds[num], i
            pp, ii, cur = prv+n, i+n, 0
            if prv == -1:
                cur = acc[1] + cnt[1]
            else:
                while pp:
                    cnt[pp] -= 1
                    acc[pp] -= prv
                    if not pp&1:
                        cur += acc[pp+1] - prv*cnt[pp+1]
                    pp >>= 1
            while ii:
                cnt[ii] += 1
                acc[ii] += i
                ii >>= 1
            sums += (cur*2 + i-prv) % mod
            res += sums % mod
        return res % mod

class SegTree:

    def __init__(self, n: int):
        self.n = 1<<n.bit_length()
        self.tree = [0]*(self.n*2)

    def update(self, ind: int, val: int):
        ind += self.n
        d = val - self.tree[ind]
        while ind:
            self.tree[ind] += d
            ind >>= 1

    def query(self, ind: int) -> int:
        if ind == -1:   return self.tree[1]
        ind += self.n
        res = 0
        while ind:
            if not ind&1:
                res += self.tree[ind+1]
            ind >>= 1
        return res