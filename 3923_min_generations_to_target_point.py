# just brute force
class Solution:
    def minGenerations(self, points: List[List[int]], target: List[int]) -> int:
        def gen(a, b):
            xa, ya, za = a
            xb, yb, zb = b
            return ((xa + xb) // 2, (ya + yb) // 2, (za + zb) // 2)
        
        def code(a):
            xa, ya, za = a
            return xa * 49 + ya * 7 + za
        
        v = [-1] * 343
        for a in points:
            ca = code(a)
            if ca == code(target):
                return 0
            v[ca] = 0
        
        g = 0
        f = True
        ct = code(target)
        while f:
            f = False
            n = len(points)
            for i in range(n-1):
                a = points[i]
                ca = code(a)
                if ca == ct:
                    break
                for j in range(i+1, n):
                    b = points[j]
                    cb = code(b)
                    if cb == ct:
                        break
                    if ca < g and cb < g:
                        continue
                    c = gen(a, b)
                    cc = code(c)
                    if v[cc] == -1:
                        v[cc] = g + 1
                        if cc == ct:
                            break
                        points.append(c)
                        f = True
            g += 1
        
        return v[ct]