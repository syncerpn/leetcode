# just check, with hash map
class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
        d = {}
        for i, c in enumerate(s):
            if c not in d:
                d[c] = i
            else:
                if i - d[c] - 1 != distance[ALPHABETS.find(c)]:
                    return False
        
        return True