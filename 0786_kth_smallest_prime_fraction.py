# heapq solution with early break
# we add fraction layer by layer
# assuming [a, b, c, d, e]
# 1st layer: a/e
# 2nd layer: a/d, b/e
# 3rd layer: a/c, b/d, c/e
# 4th layer: a/b, b/c, c/d, d/e
# one having enough k in the heapq
# we can early break the loop once we start a new layer and all values in that layer are larger than those in the heapq
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        h = []
        n = len(arr)
        c = 0
        for p in range(1,n):
            new_layer = (c == k)
            all_larger = True
            for i in range(p):
                a, b = arr[i], arr[i+n-p]
                heapq.heappush(h, (-a/b,a,b))
                c += 1
                if c > k:
                    _, x, y = heapq.heappop(h)
                    if a != x or b != y:
                        all_larger = False
                    c -= 1
            if new_layer and all_larger:
                break
        return heapq.heappop(h)[1:]

# this binary search is super fast
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        l, r = 0.0, 1.0
        
        while l < r:
            m = (l + r) / 2
            max_fraction = 0.0
            c = 0
            numerator_idx, denominator_idx = 0, 0
            j = 1
            
            for i in range(n - 1):
                while j < n and arr[i] >= m * arr[j]:
                    j += 1

                c += (n - j)

                if j == n:
                    break

                fraction = arr[i] / arr[j]

                if fraction > max_fraction:
                    numerator_idx = i
                    denominator_idx = j
                    max_fraction = fraction

            if c == k:
                return [arr[numerator_idx], arr[denominator_idx]]
            elif c > k:
                r = m
            else:
                l = m
                
        return []