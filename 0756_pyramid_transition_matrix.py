# backtracking
# might need revisit to optimize the actual runtime
class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        d = {}
        for a, b, c in allowed:
            ab = a + b
            if ab not in d:
                d[ab] = []
            d[ab].append(c)
        
        def build(s, r, i):
            if i == len(s) - 1:
                if len(r) == 1:
                    return True
                return build(r, "", 0)
            if s[i:i+2] not in d:
                return False
            for c in d[s[i:i+2]]:
                if build(s, r+c, i+1):
                    return True
            return False
        
        return build(bottom, "", 0)