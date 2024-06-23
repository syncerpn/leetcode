# count frequency with hash table then iterate the sorted key list
class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}
        for c in s:
            if c not in d:
                d[c] = 0
            d[c] += 1
        
        f = {}
        for c in d:
            n = d[c]
            if n not in f:
                f[n] = ""
            f[n] += n * c
        
        r = ""
        for i in sorted(f.keys(), reverse=True):
            r += f[i]
        return r