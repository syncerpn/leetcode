# just take one as ref and iterate
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = ''
        for i, c in enumerate(strs[0]):
            for s in strs[1:]:
                if i >= len(s):
                    return lcp
                if s[i] != c:
                    return lcp
            
            lcp += c
        
        return lcp