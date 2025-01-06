# prefix sum from the last to the first
class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        ans = ""
        A = "abcdefghijklmnopqrstuvwxyz"
        AI = {c: i for i, c in enumerate(A)}
        IA = {i: c for i, c in enumerate(A)}

        d = 0
        for i in range(len(shifts)-1, -1, -1):
            d += shifts[i]
            ans += IA[(AI[s[i]] + d) % 26]
        return ans[::-1]