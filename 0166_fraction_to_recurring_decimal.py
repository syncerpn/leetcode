# not difficult
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        sign = (numerator > 0) ^ (denominator > 0)
        i, n, d = 0, abs(numerator), abs(denominator)
        p = [n // d, "."]
        n = (n % d) * 10
        i = 2
        s = {n: i}
        ans = ""
        while n > 0:
            p.append(n // d)
            n = 10 * (n % d)
            if n in s:
                i = s[n]
                p.append(")")
                p[i:i] = "("
                ans = "".join(list(map(str, p)))
                break
            i += 1
            s[n] = i
        else:
            if p[-1] == ".":
                p.pop()
            ans = "".join(list(map(str, p)))
        
        return "-" + ans if sign else ans