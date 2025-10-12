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

# easy to understand: we track each wizard
# 1st potion: when each of them finishes the job into "done"
# 2nd potion: wizard i+1 can start working when wizard i+1 is done with the first potion and wizard i is done with the second potion
# that is max(done[i+1], done[i])
# go back and adjust done to remove any slack
class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        m, n = len(mana), len(skill)
        time = [0] * n
        for i in range(m):
            t = time[0] + mana[i] * skill[0]
            for j in range(1, n):
                t = max(t, time[j]) + mana[i] * skill[j]

            for j in range(n-1, -1, -1):
                time[j] = t
                t -= mana[i] * skill[j]


        return time[-1]