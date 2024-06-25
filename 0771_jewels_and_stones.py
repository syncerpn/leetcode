class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        c = 0
        jewels = set(jewels)
        for s in stones:
            c += s in jewels
        return c