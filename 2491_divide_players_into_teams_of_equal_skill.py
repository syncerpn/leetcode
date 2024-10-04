# fairly easy though
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        s, d = sum(skill) // (len(skill) // 2), Counter(skill)
        ans = 0
        for i in d:
            if s-i not in d or d[i] != d[s-i]:
                return -1
            ans += d[i] * i * (s-i)
        return ans // 2