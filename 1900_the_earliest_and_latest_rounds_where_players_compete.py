# barely passed lol
# we calculate beforehand, how many scenario could happen
# by calculate q, then n_scenario = 2 ** q
# handle one edge case where in the very first round firstPlayer or secondPlayer can be the one in the middle
class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        k = n
        q = 0
        if n % 2 and (firstPlayer == n // 2 + 1 or secondPlayer == n // 2 + 1):
            q += 1
        while k > 3:
            q += (k >> 1) - 2
            k = k - (k >> 1)
        
        ans = [n, 0]
        for i in range(1 << q):
            p = 1
            s = deque(range(1, n+1))
            l, r = [], []
            while s:
                if len(s) == 1:
                    s = deque(l + list(s) + r[::-1])
                    l, r = [], []
                    p += 1
                elif len(s) > 1:
                    a, b = s.popleft(), s.pop()
                    if a == firstPlayer and b == secondPlayer:
                        ans[0] = min(p, ans[0])
                        ans[1] = max(p, ans[1])
                        break
                    elif a == firstPlayer or a == secondPlayer:
                        l.append(a)
                    elif b == firstPlayer or b == secondPlayer:
                        r.append(b)
                    else:
                        j = i & 1
                        if j:
                            r.append(b)
                        else:
                            l.append(a)
                        i >>= 1
                    if not s:
                        s = deque(l + r[::-1])
                        l, r = [], []
                        p += 1
        return ans

# how about normalize the position of firstPlayer and secondPlayer after each round
# for example, n=11, f=2, s=2 after the first round
# [2, 3, 4, 5, 6, 11] -> [1(f), 2, 3(s), 4, 5, 6] with f=1, s=3
# this enables memoi
class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        @functools.cache
        def compete(k, f, s):
            if k == 2:
                return 1, 1
            if k == 3:
                if f == 1 and s == 3:
                    return 1, 1
                return 2, 2
            q = (k // 2) - 2 + (k % 2 and (f == k // 2 + 1 or s == k // 2 + 1))
            mi, ma = k, 1
            for i in range(1 << q):
                l, r = 0, 0
                a, b = 1, k
                while a < b:
                    if a == f and b == s:
                        mi = 1
                        break
                    elif a == f:
                        l += 1
                        f_next = l
                    elif a == s:
                        l += 1
                        s_next = l
                    elif b == f:
                        f_next = -r
                        r += 1
                    elif b == s:
                        s_next = -r
                        r += 1
                    else:
                        if i & 1:
                            r += 1
                        else:
                            l += 1
                        i >>= 1
                    a += 1
                    b -= 1
                else:
                    if a == b:
                        l += 1
                        if a == f:
                            f_next = l
                        elif a == s:
                            s_next = l
                    f_next = f_next if f_next > 0 else f_next + l + r
                    s_next = s_next if s_next > 0 else s_next + l + r
                    mi_n, ma_n = compete(l + r, f_next, s_next)
                    mi, ma = min(1 + mi_n, mi), max(1 + ma_n, ma)
            return mi, ma
        return compete(n, firstPlayer, secondPlayer)