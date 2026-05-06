# greedy
class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        MOD = 10 ** 9 + 7
        horizontalCuts.sort()
        verticalCuts.sort()
        a = 0
        wm = 0
        for b in verticalCuts:
            wm = max(wm, b - a)
            a = b
        wm = max(wm, w - a)

        a = 0
        wh = 0
        for b in horizontalCuts:
            wh = max(wh, b - a)
            a = b
        wh = max(wh, h - a)
        return wm * wh % MOD