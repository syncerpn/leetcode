# optimal play is to ban the one who havent used his ban power yet.
# so if R is encounter, we will try to ban the coming D
# and vice versa
# we will use queue to queue the power
# and skip those banned
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        d = r = 0
        nr = senate.count("R")
        nd = senate.count("D")
        senate = deque(senate)
        while senate and nd > 0 and nr > 0:
            s = senate.popleft()
            if s == "R":
                if d > 0:
                    d -= 1
                    nr -= 1
                else:
                    r += 1
                    senate.append(s)
            else:
                if r > 0:
                    r -= 1
                    nd -= 1
                else:
                    d += 1
                    senate.append(s)
        return "Radiant" if nr > 0 else "Dire"