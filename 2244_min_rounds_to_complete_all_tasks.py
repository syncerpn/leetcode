# easy
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        d = Counter(tasks)
        ans = 0
        for k in d:
            v = d[k]
            if v == 1:
                return -1
            q, r = v // 3, v % 3
            ans += q + int(r > 0)
        
        return ans