# op[1] is either "+" or "-", lol
# no need to care others
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for op in operations:
            if op[1] == "+":
                x += 1
            else:
                x -= 1
        return x