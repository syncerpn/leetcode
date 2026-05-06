# easy
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        d = {}
        ans = []
        for i in range(n-9):
            ss = s[i:i+10]
            if ss not in d:
                d[ss] = i
            elif d[ss] >= 0:
                ans.append(ss)
                d[ss] = -1
        return ans