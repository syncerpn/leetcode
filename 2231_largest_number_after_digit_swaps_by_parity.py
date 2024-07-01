# pure num manipulation
# sort with heapq, then unroll into the result
class Solution:
    def largestInteger(self, num: int) -> int:
        digits = []
        while num:
            digits = [num % 10] + digits
            num //= 10
        
        he = []
        ho = []
        for d in digits:
            if d % 2 == 0:
                heapq.heappush(he, -d)
            else:
                heapq.heappush(ho, -d)
        for i, d in enumerate(digits):
            if d % 2 == 0:
                digits[i] = -heapq.heappop(he)
            else:
                digits[i] = -heapq.heappop(ho)
        r = 0
        for d in digits:
            r = r * 10 + d
        return r