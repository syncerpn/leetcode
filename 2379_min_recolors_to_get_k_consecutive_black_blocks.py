# find the slice with most "B"
# recolor "W" in such slice
# count of "B" can be updated easily in O(1)
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        c = blocks[:k].count("B")
        m = c
        for i in range(len(blocks)-k):
            c = c - (blocks[i] == "B") + (blocks[i+k] == "B")
            m = max(m, c)
        return k - m