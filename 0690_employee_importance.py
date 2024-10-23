# no difference from a tree
# hash it for a quick look up
"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        d = {}
        target = None
        for eis in employees:
            d[eis.id] = eis

        r = [id]
        ans = 0
        while r:
            r_next = []
            for e in r:
                i, s = d[e].importance, d[e].subordinates
                ans += i
                r_next += s
            r = r_next
        return ans