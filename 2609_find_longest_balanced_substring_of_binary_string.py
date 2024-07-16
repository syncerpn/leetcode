# try split s into "0..01..1" partitions
# then get the max length of balanced ones
class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        t = []
        x = 0
        n = 0
        for c in s:
            if c == str(x):
                n += 1
            else:
                t.append(n)
                x = 1 - x
                n = 1
        if x == 1:
            t.append(n)
        z = 0
        for i in range(len(t) // 2):
            z = max(z, min(t[2*i], t[2*i+1]) * 2)
        return z
                