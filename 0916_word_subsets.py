# max occurence of each letter in each b of words2
# then use this counter to check each a of words1
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        d = {}
        ans = []
        for b in words2:
            db = Counter(b)
            for c in db:
                if c not in d:
                    d[c] = db[c]
                else:
                    d[c] = max(d[c], db[c])
        
        for a in words1:
            da = Counter(a)
            for c in d:
                if c not in da or da[c] < d[c]:
                    break
            else:
                ans.append(a)
        return ans