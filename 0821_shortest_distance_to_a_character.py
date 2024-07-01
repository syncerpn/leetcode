# two-pass O(n)
# first pass, try to assign distance from a character to the last index of c to the left of the considering char
# second pass, try to go backward, comparing distance of the char to its left (which is available after the first pass) and its right seen index of c
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        d = [n] * n
        last_seen = -n
        for i in range(n):
            if s[i] == c:
                last_seen = i
            d[i] = abs(i - last_seen)
        
        for i in range(n-1,-1,-1):
            if s[i] == c:
                last_seen = i
            d[i] = min(abs(last_seen - i), d[i])
        
        return d