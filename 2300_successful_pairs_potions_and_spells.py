class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        res = []
        for s in spells:
            l = 0
            r = len(potions) - 1
            while l <= r:
                m = (l + r) // 2
                if s * potions[m] < success:
                    l = m + 1
                else:
                    r = m - 1
            res.append(len(potions) - l)
        return res