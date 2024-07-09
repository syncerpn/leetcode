# there are two cases
# if arrived before previous dish is done, extra wait time should be consider
# otherwise, wait time does not change
class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        t = 0
        n = 0
        for a, w in customers:
            if n > a:
                t += n - a
            else:
                n = a
            t += w
            n += w
        return t / len(customers)