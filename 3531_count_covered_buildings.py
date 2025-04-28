# two ends of horz and vert lines
class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        r, c = {}, {}
        for x, y in buildings:
            if x not in c:
                c[x] = (y, y)
            else:
                p, q = c[x]
                c[x] = (min(p, y), max(q, y))
            
            if y not in r:
                r[y] = (x, x)
            else:
                p, q = r[y]
                r[y] = (min(p, x), max(q, x))
        
        return sum(y not in c[x] and x not in r[y] for x, y in buildings)
