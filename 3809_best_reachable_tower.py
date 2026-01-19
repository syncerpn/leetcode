# easy
class Solution:
    def bestTower(self, towers: List[List[int]], center: List[int], radius: int) -> List[int]:
        ans = (float("inf"), float("inf"), float("inf"))
        xc, yc = center
        for x, y, q in towers:
            if abs(x - xc) + abs(y - yc) <= radius:
                ans = min(ans, (-q, x, y))
        
        return [ans[1], ans[2]] if ans[0] < float("inf") else [-1, -1]