# easy
class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        ans = -1
        for i, a in enumerate(capacity):
            if a >= itemSize:
                if ans == -1 or a < capacity[ans]:
                    ans = i
        return ans