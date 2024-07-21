# we have to collect all garbages, so just take length of sum of garbage string
# we need to find the last house each G P M truck has to arrive to calculate the distance
class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        n = len(garbage)
        g, p, m = 0, 0, 0
        s = ""
        for i in range(n-1,-1,-1):
            s += garbage[i]
            if not g and "G" in garbage[i]:
                g = i
            if not p and "P" in garbage[i]:
                p = i
            if not m and "M" in garbage[i]:
                m = i
        
        ans = len(s)
        for i in range(1, len(travel)):
            travel[i] += travel[i-1]
        if g:
            ans += travel[g-1]
        if p:
            ans += travel[p-1]
        if m:
            ans += travel[m-1]
        return ans