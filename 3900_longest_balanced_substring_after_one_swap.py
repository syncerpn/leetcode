# not as easy as it looks
# it looks like a binary search prob
# but binary search wont work
# instead use prefix hash
# we process it with the same logic
# either the window has the same number of zeros and ones
# or the difference is exactly two
# plus there are extra element outside the window to be swapped
class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        z, o, d = [0] * n, [0] * n, [0] * n
        cnt0 = cnt1 = 0

        for i in range(n):
            if s[i] == '0': cnt0 += 1
            else: cnt1 += 1
            z[i], o[i], d[i] = cnt0, cnt1, cnt1 - cnt0

        ans = 0
        ind, ind0, ind1 = {0: -1}, {}, {}

        for i in range(n):
            pref = d[i]
            if pref in ind:
                ans = max(ans, i - ind[pref])
            
            if (pref + 2) in ind:
                j = ind[pref + 2]
                sub1s = o[i] - (o[j] if j >= 0 else 0)
                if cnt1 > sub1s: ans = max(ans, i - j)
                elif (pref + 2) in ind1: ans = max(ans, i - ind1[pref + 2])
            
            if (pref - 2) in ind:
                j = ind[pref - 2]
                sub0s = z[i] - (z[j] if j >= 0 else 0)
                if cnt0 > sub0s: ans = max(ans, i - j)
                elif (pref - 2) in ind0: ans = max(ans, i - ind0[pref - 2])
            
            if pref not in ind: ind[pref] = i
            if pref not in ind0 and z[i] > 0: ind0[pref] = i
            if pref not in ind1 and o[i] > 0: ind1[pref] = i

        return ans