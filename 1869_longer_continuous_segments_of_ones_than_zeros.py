# python makes it easy
class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        z = max([len(p) for p in s.split("1")])
        o = max([len(p) for p in s.split("0")])
        return o > z

# or simply track it by yourself
class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        o = 0
        z = 0
        o_max = 0
        z_max = 0
        for c in s:
            if c == "1":
                o += 1
                z_max = max(z, z_max)
                z = 0
            else:
                z += 1
                o_max = max(o, o_max)
                o = 0
        
        z_max = max(z, z_max)
        o_max = max(o, o_max)
        return o_max > z_max