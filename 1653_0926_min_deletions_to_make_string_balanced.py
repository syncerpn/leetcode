# same as #0926
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

# much better simplified solution
# once encounter an "a", we may choose to delete one more "a" or all "b" found so far
# pick either way with smaller move
class Solution:
    def minimumDeletions(self, s: str) -> int:
        ans = 0
        b = 0
        for c in s:
            if c == "a":
                ans = min(b, ans+1)
            else:
                b += 1
        return ans