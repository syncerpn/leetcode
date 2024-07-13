# count and check all string with count == 1
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d = {}
        for a in arr:
            if a not in d:
                d[a] = 0
            d[a] += 1
        
        for a in arr:
            if d[a] == 1:
                k -= 1
                if k == 0:
                    return a
        return ""