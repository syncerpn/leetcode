# solved but forgot to add comments
# it is greedy btw
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = {}
        for i, c in enumerate(s):
            d[c] = i
        ans = []
        k = 0
        j = 0
        for i, c in enumerate(s):
            j = max(j, d[c])
            if j == i:
                ans.append(j-k+1)
                k = j + 1
        return ans

# ordered dict for convenience
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = OrderedDict()
        for i, c in enumerate(s):
            if c not in d:
                d[c] = [i, i]
            d[c][1] = i
        
        ans = []
        l, r = 0, 0
        for c in d:
            if d[c][0] > r:
                ans.append(r-l+1)
                l, r = d[c]
            elif d[c][1] >= r:
                r = d[c][1]
        
        ans.append(r-l+1)
        return ans