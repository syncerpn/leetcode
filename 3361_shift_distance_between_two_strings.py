# prefix sum and greedy
# we simply just want to move in one direction
# i.e. either move next or more previous until the two characters match
# choose whichever way that costs less
class Solution:
    def shiftDistance(self, s: str, t: str, nextCost: List[int], previousCost: List[int]) -> int:
        d = 0
        acc_next = [0]
        for c in nextCost:
            d += c
            acc_next.append(d)
        
        d = 0
        acc_prev = [0]
        for c in previousCost[::-1]:
            d += c
            acc_prev.append(d)
        
        ans = 0
        for a, b in zip(s, t):
            if a == b:
                continue
            elif b > a:
                ans += min(acc_next[ord(b)-97] - acc_next[ord(a)-97], acc_prev[-1] + acc_prev[122-ord(b)] - acc_prev[122-ord(a)])
            else:
                ans += min(acc_next[ord(b)-97] - acc_next[ord(a)-97] + acc_next[-1], acc_prev[122-ord(b)] - acc_prev[122-ord(a)])
        return ans