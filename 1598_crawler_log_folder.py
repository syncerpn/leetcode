# simple navigation
# not even need stack
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        d = 0
        for op in logs:
            if op == "../":
                if d > 0:
                    d -= 1
            elif op != "./":
                d += 1
        
        return d