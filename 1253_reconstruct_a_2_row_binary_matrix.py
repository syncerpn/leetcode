# easy
class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        m = len(colsum)
        ans = [[0] * m for _ in range(2)]
        for i in range(m):
            if colsum[i] == 2:
                if upper > 0 and lower > 0:
                    ans[0][i] = 1
                    ans[1][i] = 1
                    upper -= 1
                    lower -= 1
                else:
                    return []
            elif colsum[i] == 0:
                continue
            else:
                if upper >= lower and upper > 0:
                    upper -= 1
                    ans[0][i] = 1
                elif lower > upper >= 0:
                    lower -= 1
                    ans[1][i] = 1
                else:
                    return []
        if upper > 0 or lower > 0:
            return []
        return ans