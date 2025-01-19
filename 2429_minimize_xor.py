# greedily set msb bits to 1 if possible
class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        m = bin(num2).count("1")
        s = bin(num1)[2:]
        n = s.count("1")
        
        if m >= len(s):
            return (1 << m) - 1
        
        ans = []
        for c in s:
            if c == "1" and m > 0:
                ans.append(1)
                m -= 1
            else:
                ans.append(0)
        i = -1
        while m > 0:
            if ans[i] == 0:
                ans[i] = 1
                m -= 1
            i -= 1
        
        l = len(ans)
        return sum(a << (l-1-i) for i, a in enumerate(ans))