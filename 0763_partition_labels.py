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