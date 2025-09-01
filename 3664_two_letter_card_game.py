# groups into xx, *x and x*
# in *x and x*, the most frequent card affects the pairing
# because if it is too large, some will be left unpaired
# so the best pairing in x* and *x can be calculated
# by min(s - m, s // 2) where s is total, m is largest frequency
# the unpaired cards from both *x and x* are now paired with wildcards
# that gives us min(wilds, free) more points
# after this step, this is the missing logic in my original algorithm
# if we still have more than 2 wildcards
# you can make 2 pairs out of each pair in x* or *x
# just by breaking it into xa+xx and xb+xx, or ax+xx and bx+xx for example
# that give us 1 more point for each breaking down
class Solution:
    def score(self, cards: List[str], x: str) -> int:
        wilds = 0
        countL = [0] * 10
        countR = [0] * 10
        for a, b in cards:
            if a == b == x:
                wilds += 1
            elif a == x:
                countL[ord(b) - 97] += 1
            elif b == x:
                countR[ord(a) - 97] += 1

        pairs = free = 0
        for count in [countL, countR]:
            s = sum(count)
            m = max(count)
            p = min(s - m, s // 2)
            pairs += p
            free += s - 2 * p
        
        used = min(wilds, free)
        wilds -= used
        extra = min(pairs, wilds // 2)
        return pairs + used + extra