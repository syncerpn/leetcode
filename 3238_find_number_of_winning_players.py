# simple counting
class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        d = {}
        ans = set()
        for i, c in pick:
            if i not in d:
                d[i] = {}
            if c not in d[i]:
                d[i][c] = 0
            d[i][c] += 1
            if d[i][c] > i:
                ans.add(i)
        return len(ans)