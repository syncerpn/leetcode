# should be easy
# implementation is a bit cumbersome
class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reservedSeats.sort()
        reservedSeats.append([n+1, 0])
        r, a, b, c = 0, False, False, False
        ans = 0
        for s, q in reservedSeats:
            if s != r:
                ans += 2 * (s - r - 1)
                if a and c:
                    ans += 2
                elif not (a or b or c):
                    ans += 0
                else:
                    ans += 1
                a, b, c = True, True, True
            if q == 2 or q == 3:
                a = False
            elif q == 4 or q == 5:
                a = False
                b = False
            elif q == 6 or q == 7:
                b = False
                c = False
            elif q == 8 or q == 9:
                c = False
            r = s
        
        return ans