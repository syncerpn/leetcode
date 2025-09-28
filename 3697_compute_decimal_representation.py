# string for easy implementation in python
class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        s = str(n)
        l = len(s)
        return [int(c) * 10 ** (l-i-1) for i, c in enumerate(s) if c != "0"]