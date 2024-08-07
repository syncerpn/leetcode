# if go greedy path
# it becomes pure math
class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        n = len(grades)
        return (int((n * 8 + 1) ** 0.5) - 1) // 2