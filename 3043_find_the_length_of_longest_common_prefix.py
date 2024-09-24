# trie
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        r = {}
        for a in arr1:
            s = str(a)
            n = r
            for c in s:
                if c not in n:
                    n[c] = {}
                n = n[c]
        
        ans = 0
        for a in arr2:
            s = str(a)
            n = r
            i = 0
            for c in s:
                if c not in n:
                    break
                n = n[c]
                i += 1
            ans = max(ans, i)
        return ans