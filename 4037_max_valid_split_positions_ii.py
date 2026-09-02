# actual logic here to reduce this from O(n2logV) to O(nlogV ?)
# is that gcd if changes will change very fast (by at least a factor of 2)
# so, we only need to attempt removing the index at the border (of two different gcd) of prefix
class Solution:
    def maxValidSplits(self, nums: list[int]) -> int:
        def solve(pre: List[int], suff: List[int], skip: int, a: List[int]) -> int:
            n = len(a)
            for i in range(1, n + 1):
                if i - 1 == skip:
                    pre[i] = pre[i - 1]
                    continue
                pre[i] = gcd(pre[i - 1], a[i - 1])
            for i in range(n - 1, -1, -1):
                if i == skip:
                    suff[i] = suff[i + 1]
                    continue
                suff[i] = gcd(suff[i + 1], a[i])
            curr = 0
            for i in range(n - 1):
                if i == skip:
                    continue
                if pre[i + 1] == suff[i + 1]:
                    curr += 1
            return curr

        n = len(nums)
        ans = 0
        premain = [0] * (n + 1)
        suffmain = [0] * (n + 1)
        for i in range(1, n + 1):
            premain[i] = gcd(premain[i - 1], nums[i - 1])
        for i in range(n - 1, -1, -1):
            suffmain[i] = gcd(suffmain[i + 1], nums[i])

        for i in range(n + 1):
            if i > 0 and premain[i] == premain[i - 1]:
                continue
            skip = i - 1
            pre = [0] * (n + 1)
            suff = [0] * (n + 1)
            ans = max(ans, solve(pre, suff, i - 1, nums))

        for i in range(n - 1, -1, -1):
            if suffmain[i] == suffmain[i + 1]:
                continue
            pre = [0] * (n + 1)
            suff = [0] * (n + 1)
            skip = i - 1
            ans = max(ans, solve(pre, suff, i - 1, nums))

        return ans

# from other users in #4035
# still works in this one
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