# O(m) solution where m is length of s
# we use hash table to quickly find out the first instruction that makes the robot goes out of grid
# the hash table stores prefix-sum/accumulated position difference from starting position
# also remember to adjust this position difference every time the suffix changes its starting character
class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        vpos, hpos = {}, {}
        v, h = 0, 0
        m = len(s)
        # build the hash table with prefix sum for each dimension
        for i, c in enumerate(s):
            if   c in "LR":
                h += 1 if c == "R" else -1
                if h not in hpos:
                    hpos[h] = []
                hpos[h].append(i)
            else:
                v += 1 if c == "D" else -1
                if v not in vpos:
                    vpos[v] = []
                vpos[v].append(i)
        
        vs, hs = startPos
        ans = [0] * m
        for i, c in enumerate(s):
            k = m
            # find the first instruction that moves the robot out of grid
            # optimized/compressed code to search all 4 borders with template loop
            for pos, p in zip((vpos, vpos, hpos, hpos), (-1-vs, n-vs, -1-hs, n-hs)):
                if p in pos and pos[p]:
                    while pos[p] and pos[p][0] < i:
                        pos[p].pop(0)
                    if pos[p]:
                        k = min(k, pos[p][0])

            # instructions from i upto k should be executable
            ans[i] = k - i
            
            # adjust position difference every time the suffix changes its starting character
            vs += -1 if c == "D" else (1 if c == "U" else 0)
            hs += -1 if c == "R" else (1 if c == "L" else 0)
        return ans