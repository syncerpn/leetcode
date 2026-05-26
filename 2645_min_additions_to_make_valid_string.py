# state machine
class Solution:
    def addMinimum(self, word: str) -> int:
        p = "c"
        ans = 0
        for c in word:
            if p == c:
                ans += 2
            elif p == "c" and c == "b":
                ans += 1
            elif p == "a" and c == "c":
                ans += 1
            elif p == "b" and c == "a":
                ans += 1
            p = c
        if p == "a":
            ans += 2
        if p == "b":
            ans += 1
        return ans

# shorter impl
class Solution:
    def addMinimum(self, word: str) -> int:
        d = {"a": 0, "b": 1, "c": 2}
        p = "c"
        ans = 0
        for c in word:
            ans += (d[c] - d[p] + 2) % 3
            p = c
        ans += d["c"] - d[p]
        return ans