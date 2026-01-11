# calculating the cost is quite tricky
# other than that, we can greedily set the bit from high to low
class Solution:
    def maximumAND(self, nums: List[int], k: int, m: int) -> int:
        ans = 0
        for i in range(31, -1, -1):
            t = ans | (1 << i)
            h = []
            c_sum = 0
            for a in nums:
                c = 0
                r = t & ~a
                if r:
                    b = r.bit_length() - 1
                    while (a >> b) & 1:
                        b += 1
                    mask = (1 << b) - 1
                    c = (a & ~mask | (1 << b) | (t & mask)) - a
                heapq.heappush(h, -c)
                c_sum += c
                if len(h) > m:
                    c_sum += heapq.heappop(h)
            if c_sum <= k:
                ans = t
        
        return ans