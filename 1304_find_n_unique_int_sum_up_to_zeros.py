# array from -(n//2) to n//2 should work
# insertion of 0 depends on whether n is odd or even
class Solution:
    def sumZero(self, n: int) -> List[int]:
        return list(range(-(n//2), n%2)) + list(range(1, n//2+1))