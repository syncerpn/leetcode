# binary search because solutions are easy to valid
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def can_distribute(k):
            j = 0
            c = 1
            for i in range(1, len(position)):
                if position[i] - position[j] >= k:
                    c += 1
                    j = i
                    if c == m:
                        return True
            
            return False

        position.sort()
        if m == 2:
            return position[-1] - position[0]

        l = 1
        r = (position[-1] - position[0]) // (m - 1) + 1
        while l + 1 < r:
            k = (l + r) // 2
            if can_distribute(k):
                l = k
            else:
                r = k
        
        return l