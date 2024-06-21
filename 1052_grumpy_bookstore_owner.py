# sliding windows is fine; this one is fairly easy
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        extra = 0
        extra_max = 0
        total = 0
        for i, n in enumerate(customers):
            total += n * (1 - grumpy[i])
            if i < minutes:
                extra += grumpy[i] * n
                extra_max = extra
            else:
                extra += grumpy[i] * n - grumpy[i-minutes] * customers[i-minutes]
                if extra > extra_max:
                    extra_max = extra
        
        return total + extra_max