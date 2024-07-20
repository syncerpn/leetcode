# recursive solution
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        s = self.countAndSay(n-1)
        n = 1
        p = s[0]
        r = ""
        for c in s[1:]:
            if c == p:
                n += 1
            else:
                r += str(n) + p
                p = c
                n = 1
        r += str(n) + p
        return r

# iterative solution
# not so much different, really
class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        for _ in range(n-1):
            n = 1
            p = s[0]
            r = ""
            for c in s[1:]:
                if c == p:
                    n += 1
                else:
                    r += str(n) + p
                    p = c
                    n = 1
            r += str(n) + p
            s = r
        return s