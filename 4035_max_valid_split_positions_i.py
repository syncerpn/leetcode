# brute force version O(n2logV)
class Solution:
    def maxValidSplits(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0
        for k in range(n+1):
            F = [0]
            for i in range(n):
                if i == k:
                    continue
                F.append(math.gcd(F[-1], nums[i]))
            
            b = 0
            t = 0
            for i in range(n-1, -1, -1):
                if i == k:
                    continue
                if b == F.pop():
                    t += 1
                b = math.gcd(b, nums[i])
            ans = max(ans, t)
        return ans

# very fast one
# actually is the solution to the harder version #4037
class Solution:
    def maxValidSplits(self, nums: list[int]) -> int:
        n = len(nums)

        pg, sg = [0] * (n+1), [0] * (n+1)
        for i in range(n):
            pg[i+1] = gcd(pg[i], nums[i])
        for i in reversed(range(n)):
            sg[i] = gcd(sg[i+1],nums[i])

        ans =0
        for i in range(1, n):
            if pg[i]==sg[i]:
                ans += 1
        if n <= 2:
            return ans

        wh = pg[n]
        m = n - 1
        for elim in range(n):
            t = gcd(pg[elim], sg[elim+1])
            if t <= wh:
                continue
            pg_ = [0]*m
            pr, pw = 0, 0
            for i in range(n):
                if i == elim:
                    continue
                pr = gcd(pr, nums[i])
                pg_[pw] = pr
                pw += 1
            cur = 0
            pr = 0
            pw = m - 1
            for i in reversed(range(n)):
                if i == elim:
                    continue
                pr = gcd(pr, nums[i])
                if pw and pg_[pw - 1] == pr:
                    cur+=1
                pw -= 1
            ans = max(ans, cur)

        return ans