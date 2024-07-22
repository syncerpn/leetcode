# exact result
# but can be converted into n * n // 4 with integer division
class Solution:
    def minOperations(self, n: int) -> int:
        return (n * n - (n & 1)) // 4