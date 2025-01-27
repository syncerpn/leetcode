# also need revisit because i was busy
# also not optimal solution anyway
# check out topology sort
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        g = [[False] * numCourses for _ in range(numCourses)]

        for i, j in prerequisites:
            g[i][j] = True

        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    g[i][j] = g[i][j] or (g[i][k] and g[k][j])

        return [g[i][j] for i, j in queries]