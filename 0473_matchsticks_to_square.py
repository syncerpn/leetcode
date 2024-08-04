# for general problem, see #0698
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        matchsticks.sort(reverse=True)
        s = sum(matchsticks)
        a = s // 4
        if a * 4 != s:
            return False
        b = [0] * 4
        def dfs(i):
            if i == len(matchsticks):
                return len(set(b)) == 1
            for j in range(4):
                b[j] += matchsticks[i]
                if b[j] <= a and dfs(i+1):
                    return True
                b[j] -= matchsticks[i]
                if b[j] == 0:
                    break
            return False
        return dfs(0)
        