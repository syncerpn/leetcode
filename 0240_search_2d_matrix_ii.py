# O(mn) with bfs/dfs
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        v = [[False] * n for _ in range(m)]
        s = [[0, 0]]
        while s:
            i, j = s.pop()
            v[i][j] = True
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                if i + 1 < m and not v[i+1][j]:
                    s.append((i+1, j))
                if j + 1 < n and not v[i][j+1]:
                    s.append((i, j+1))
            else:
                if i - 1 >= 0 and not v[i-1][j]:
                    s.append((i-1, j))
                if j - 1 >= 0 and not v[i][j-1]:
                    s.append((i, j-1))
        return False

# O(m + n): search from top right or bottom left
# we may eliminate a whole row or col each case
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n-1

        while i < m and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                i += 1
            else:
                j -= 1
        return False