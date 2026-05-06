# stack
class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        P = sorted(list(zip(indices, sources, targets)))
        l = 0
        ans = []
        for i, a, b in P:
            k = len(a)
            if s[i:i+k] == a:
                ans.append(s[l:i])
                l = i + k
                ans.append(b)
        ans.append(s[l:])
        return "".join(ans)