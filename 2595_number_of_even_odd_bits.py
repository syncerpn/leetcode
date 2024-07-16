# make it bitwise
class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        even = 0
        odd = 0
        even_index = 1
        while n:
            even += even_index and (n & 1)
            odd += (not even_index) and (n & 1)
            n = n >> 1
            even_index = not even_index
        return [even, odd]
