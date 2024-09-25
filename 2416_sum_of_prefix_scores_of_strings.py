# trie
# if you know it, this is probably an easy one
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        r = {}
        for word in words:
            n = r
            for c in word:
                if c not in n:
                    n[c] = [0, {}]
                n[c][0] += 1
                n = n[c][1]
        
        ans = []
        for word in words:
            n = r
            t = 0
            for c in word:
                t += n[c][0]
                n = n[c][1]
            ans.append(t)
        return ans