# easy with two hashmap
class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        k = {}
        d = {}
        ans = []
        for i, c in queries:
            if i in d:
                p = d[i]
                k[p] -= 1
                if k[p] == 0:
                    del k[p]
            d[i] = c
            if c not in k:
                k[c] = 1
            else:
                k[c] += 1
            ans.append(len(k))
        
        return ans