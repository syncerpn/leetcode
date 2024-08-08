# prefix and accumulate
# greedy, of course
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        if satisfaction[0] <= 0:
            return 0
        n = len(satisfaction)
        p = 0
        for i in range(n):
            p += satisfaction[i]
            satisfaction[i] = p
        p = 0
        for i in range(n):
            p += satisfaction[i]
            satisfaction[i] = p
        return max(satisfaction)