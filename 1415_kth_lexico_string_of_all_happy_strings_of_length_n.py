# math shines
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        H = {"a": ["b", "c"], "b": ["a", "c"], "c": ["a", "b"]}
        
        m = 1 << (n-1)
        k -= 1

        d = k // m
        if d > 2:
            return ""
        s = "a" if d == 0 else ("b" if d == 1 else "c")
        
        n -= 1
        while n:
            k %= m
            m >>= 1
            s += H[s[-1]][k // m]
            n -= 1
        
        return s