# greedily choose largest boxes first
class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        a = sum(apple)
        capacity.sort(reverse=True)
        b = 0
        m = 0
        for c in capacity:
            b += c
            m += 1
            if b >= a:
                return m
        return m