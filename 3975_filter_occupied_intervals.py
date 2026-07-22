# easy
class Solution:
    def filterOccupiedIntervals(self, occupiedIntervals: List[List[int]], freeStart: int, freeEnd: int) -> List[List[int]]:
        occupiedIntervals.sort()
        ans = []

        def free(x, y):
            if freeStart <= x and y <= freeEnd:
                return
            elif x < freeStart and y > freeEnd:
                ans.append((x, freeStart - 1))
                ans.append((freeEnd + 1, y))
            elif freeStart <= x <= freeEnd:
                ans.append((freeEnd + 1, y))
            elif freeStart <= y <= freeEnd:
                ans.append((x, freeStart - 1))
            else:
                ans.append((x, y))

        x, y = occupiedIntervals[0]
        for a, b in occupiedIntervals:
            if a > y + 1:
                free(x, y)
                x, y = a, b
            else:
                y = max(y, b)
        free(x, y)
        return ans