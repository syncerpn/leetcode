# boil down to xy and yx pairs
# (of course we dont need to touch xx and yy pairs)
# so we can pair 2 xy (or 2 yx) to make one swap
# if there exist unpaired xy and yx at the end
# we need 2 swaps
class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        x1 = s1.count("x")
        x2 = s2.count("x")
        if (x1 + x2) % 2:
            return -1
        xy, yx = 0, 0
        for a, b in zip(s1, s2):
            if a == b:
                continue
            if a == "x":
                xy += 1
            else:
                yx += 1
        
        return xy // 2 + yx // 2 + (xy % 2) * 2
