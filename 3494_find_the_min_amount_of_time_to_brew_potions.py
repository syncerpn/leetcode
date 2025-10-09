# need revisit
class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n, m = len(skill), len(mana)
        p = [0] * n
        for i in range(1, n):
            p[i] = p[i - 1] + skill[i]

        t = skill[0] * mana[0]

        for j in range(1, m):
            tm = skill[0] * mana[j]
            for i in range(1, n):
                d = p[i] * mana[j - 1] - p[i - 1] * mana[j]
                if d > tm:
                    tm = d
            t += tm

        return t + p[-1] * mana[-1]
        