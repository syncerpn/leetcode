# nice problem, and solution as well
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        # we define a function to check whether it is possible to make m bouquets of k consecutive flowers
        def check(d, bloomDay, m, k):
            n_bouquets = 0
            c = 0
            for b in bloomDay:
                if b > d:
                    c = 0
                    continue
                
                c += 1
                if c == k:
                    n_bouquets += 1
                    c = 0
                    if n_bouquets == m:
                        return True
            
            return False
        
        # if the number of flowers is not enough, we cant make enough bouquets
        if m * k > len(bloomDay):
            return -1

        # otherwise, there is always a way to make it
        # use, binary search to find the min number of days
        l = 1
        r = max(bloomDay)
        while l < r:
            d = (l + r) // 2
            if check(d, bloomDay, m, k):
                r = d
            else:
                l = d + 1
        # return the last one satified
        return r