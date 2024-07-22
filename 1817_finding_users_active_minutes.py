# easy
class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        ans = [0] * k
        d = {}
        for i, m in logs:
            if i not in d:
                d[i] = set()
            d[i].add(m)

        for i in d:
            ans[len(set(d[i]))-1] += 1
        return ans