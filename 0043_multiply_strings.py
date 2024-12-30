# stupid question
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        m, n = len(num1), len(num2)
        d = Counter()
        for i in range(m):
            for j in range(n):
                d[i+j] += int(num1[m-1-i])*int(num2[n-1-j])
                
        carry, ans = 0, ""
        for i in range(m+n-1):
            carry, digit = divmod(carry + d[i], 10)
            ans += str(digit)
            
        ans = (str(carry) + ans[::-1]).lstrip("0")
        return ans if ans != "" else "0"
        