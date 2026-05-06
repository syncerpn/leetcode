# easy
class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        m = len(s) // k
        return Counter([s[i*m:i*m+m] for i in range(k)]) == Counter([t[i*m:i*m+m] for i in range(k)])