# generate all base-10 mirror nums
# then check if they are mirror nums in base-k
class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def gen_mirror_num(s, d):
            if d:
                p = s + s[-2::-1]
            else:
                p = s + s[-1::-1]
            n = len(s)
            s[-1] += 1
            for i in range(n):
                if s[~i] == 10:
                    s[~i] = 0
                    if i < n - 1:
                        s[~(i+1)] += 1
                    else:
                        d = not d
                        if d:
                            s.append(0)
                            s[0] = 1
                        else:
                            s[~i] = 1
            return sum(a * 10 ** i for i, a in enumerate(p)), d

        def is_mirror(p, k):
            q = []
            while p > 0:
                q.append(p % k)
                p //= k
            for i in range(len(q) // 2):
                if q[i] != q[~i]:
                    return False
            return True

        d = True
        s = [1]

        ans = 0
        while n > 0:
            p, d = gen_mirror_num(s, d)
            if is_mirror(p, k):
                ans += p
                n -= 1
        return ans