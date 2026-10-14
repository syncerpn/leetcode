# gut feeling tells that merge can be done easily by check whether left robot is going faster than the consecutive right one
# and it is true after tests
# this is my 2-pass implementation
# distance merge first
# then speed merge later
class Solution:
    def countGroups(self, position: list[int], speed: list[int], distance: int) -> int:
        P = []
        S = []
        q, r = -inf, -inf
        for p, s in zip(position, speed):
            if p - q <= distance:
                P.pop()
                S.pop()
            P.append(p)
            S.append(s)

            q, r = p, s

        q, r = inf, inf
        ans = 0
        while S:
            p = P.pop()
            s = S.pop()
            if s <= r:
                q, r = p, s
                ans += 1
        
        return ans

# actually, we can do it 1-pass efficiently
class Solution:
    def countGroups(self, position: list[int], speed: list[int], distance: int) -> int:
        q, r = inf, inf
        ans = 0
        while position:
            p = position.pop()
            s = speed.pop()
            if s <= r and q - p > distance:
                r = s
                ans += 1
            q = p
        
        return ans