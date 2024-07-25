# segment sums
class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        def segment(row):
            s = {}
            x = 0
            l = 0
            for i, k in enumerate(row + [0]):
                if k:
                    l += 1
                else:
                    if l > 0:
                        s[x] = [l, 1]
                    x = i + 1
                    l = 0
            return s
        
        def add(s, a):
            r, rec = {}, []
            for j in s:
                if j not in a:
                    rec.append([j] + s[j])
                    
            for i in a:
                if i in s:
                    w, h = s[i]
                    r[i] = [w, h+1]
                elif i not in r:
                    w, h = a[i]
                    r[i] = [w, h]
            
            return r, rec
                    
        res = []
        acc = {}
        for r, row in enumerate(land + [[0]]):
            acc, rec = add(acc, segment(row))
            for c, w, h in rec:
                res.append([r-h, c, r-1, c+w-1])
        
        return res