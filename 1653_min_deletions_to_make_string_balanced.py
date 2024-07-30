# count subarrays of only a and b
# pairing deletion
class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = 0
        p = "a"
        a = []
        b = []
        for c in s + "#":
            if c != p:
                if p == "a":
                    a.append(n)
                else:
                    b.append(n)
                n = 0
            n += 1
            p = c
        if len(b) < len(a):
            b.append(0)
        for i in range(len(a)-2, -1, -1):
            a[i] = a[i] + a[i+1]
        a.append(0)
        for i in range(1, len(b)):
            b[i] = b[i] + b[i-1]
        b = [0] + b
        ans = len(s)
        for p, q in zip(a[1:], b[:-1]):
            ans = min(ans, p + q)
        return ans