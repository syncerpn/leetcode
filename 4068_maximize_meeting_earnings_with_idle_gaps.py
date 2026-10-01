# feel good solving this problem
# actually it looks solvable at the first place
# first, we sort things by end time as usual with scheduling problem
# then we will consider score up to an end time
# score should take into account the gap earning as well
# save the candidate into a sorted list and use binary search to find the one we can merge
# important point is that, score advantage should be rewarded to those end earlier
# if one ends later, it should make sure that the revenue is large enough to become a candidate
# for example:
# - compare (ending, revenue) pairs (1, 4) and (2, 5), pair (1, 4) takes the advantage because of early ending
# - compare (ending, revenue) pairs (1, 4) and (2, 6), pair (2, 6) can be a candidate even though it ends later
# because if a pair (a, any) to be merged with both, the total revenues are 4 + a - 1 vs. 6 + a - 2
# then definitely 6 + a - 2 > 4 + a - 1, a better revenue
class Solution:
    def maxEarnings(self, meetings: list[list[int]]) -> int:
        meetings.sort(key=lambda x: (x[1]))
        E = []
        R = {}
        ans = meetings[0][2]

        for a, b, r in meetings:
            if not E:
                E.append(b)
                R[b] = r
            else:
                r_total = r
                i = bisect.bisect_right(E, a + 0.5)
                if i > 0:
                    e = E[i-1]
                    r_total += R[e] + a - e
                ans = max(ans, r_total)
                while E and E[-1] >= b and R[E[-1]] - E[-1] < r_total - b:
                    e = E.pop()
                    del R[e]
                if not E or (E and E[-1] < b and R[E[-1]] - E[-1] < r_total - b):
                    E.append(b)
                    R[b] = r_total
        return ans