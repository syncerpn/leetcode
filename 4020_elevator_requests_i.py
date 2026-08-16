# easy
class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        return sum(abs(a - b) for a, b in pairwise(requests)) + requests[0]