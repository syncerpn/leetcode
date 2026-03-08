# fairly easy with a hard-tagged problem
# can be solved with prefix sum
class Solution:
    def minCost(self, s: str, encCost: int, flatCost: int) -> int:
        p = [0]
        for c in s:
            if c == "0":
                p.append(p[-1])
            else:
                p.append(p[-1] + 1)
        def helper(i, j):
            x = p[j] - p[i]
            l = j - i
            cost = flatCost if x == 0 else x * l * encCost
            if l % 2:
                return cost
            else:
                return min(cost, helper(i, (j + i) // 2) + helper((j + i) // 2, j))
        return helper(0, len(s))