# handling cases of consecutive 0s or 1s differently
class Solution:
    def minOperations(self, n: int) -> int:
        while n and n % 2 == 0:
            n >>= 1

        b = bin(n)[2:]
        print(b)
        p = 0
        s = ""
        ans = 0
        for c in b:
            if c == "0":
                p += 1
            else:
                if p == 1:
                    s += "0"
                p = 0

            if p == 0:
                s += c
            elif p > 1:
                ans += min(s.count("0") + 2, s.count("1"))
                s = ""
        if s:
            ans += min(s.count("0") + 2, s.count("1"))
        return ans