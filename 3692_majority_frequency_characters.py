# easy
class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        d = Counter(s)
        e = {}
        for k in d:
            v = d[k]
            if v not in e:
                e[v] = (0, v, "")
            l, _, r = e[v]
            e[v] = l + 1, v, r + k
        _, _, ans = max(e.values())
        return ans