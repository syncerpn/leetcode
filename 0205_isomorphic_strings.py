# simple hash table should do
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ms = {}
        mt = {}
        for cs,ct in zip(s,t):
            if cs in ms:
                if ct != ms[cs]:
                    return False
            else:
                if ct in mt:
                    return False
                ms[cs] = ct
                mt[ct] = cs
        
        return True