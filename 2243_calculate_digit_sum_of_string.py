# try simulate the process
class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            if len(s) % k:
                s += "0" * (k - len(s) % k)
            t = ""
            p = int(s[0])
            i = 1
            while i < len(s):
                if i % k == 0:
                    t += str(p)
                    p = 0
                p += int(s[i])
                i += 1
            t += str(p)
            s = t
        return s