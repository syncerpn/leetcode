# interval
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        d = [0] * (len(s) + 1)
        for a, b, c in shifts:
            d[a]   += (c << 1) - 1
            d[b+1] += -((c << 1) - 1)
        
        for i in range(1, len(d)):
            d[i] += d[i-1]

        ans = ""
        A = "abcdefghijklmnopqrstuvwxyz"
        AI = {c: i for i, c in enumerate(A)}
        IA = {i: c for i, c in enumerate(A)}

        for i, c in enumerate(s):
            ans += IA[(AI[c] + d[i]) % 26]
        return ans