# stack count + greedy for max score
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if y > x:
            return self.maximumGain(s[::-1], y, x)
        
        # count for each "a" and "b" encountered so far
        ra = 0
        rb = 0
        score = 0
        for c in s + "#":
            # empty the stack count when a character is not "a" or "b"
            if c != "a" and c != "b":
                # the remaining "a" and "b" can form some pairs "ba"
                score += min(ra, rb) * y
                ra = 0
                rb = 0
            elif c == "b":
                # if it is "b", and we have some "a" to spend
                # spend it now for maximum score
                if ra > 0:
                    score += x
                    ra -= 1
                # or we save it for "ba" pair
                else:
                    rb += 1
            else:
                # save "a" for later use
                ra += 1
        return score