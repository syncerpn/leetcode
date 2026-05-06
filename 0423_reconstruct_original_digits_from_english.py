# nice problem
# suggest some kinds of great encoding/encrypting
# beautifully implemented by myself lol
class Solution:
    def originalDigits(self, s: str) -> str:
        ans = [0] * 10
        d = Counter(list(s))
        S = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        R = ["z", "o", "w", "r", "f", "v", "x", "s", "h", "i"]
        I = [0, 2, 6, 7, 5, 4, 3, 8, 1, 9]
        for i in I:
            r = R[i]
            s = S[i]
            if d[r] > 0:
                k = d[r]
                ans[i] += k
                for c in s:
                    d[c] -= k
        return "".join(str(i) * ans[i] for i in range(10))