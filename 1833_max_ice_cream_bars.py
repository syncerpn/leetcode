# sorting is trivial
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        n = 0
        for c in costs:
            coins -= c
            if coins < 0:
                break
            n += 1
        return n

# counting sort solution
# but why a must? what a waste of space
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        CONSTRAINTS_MAX = 100001
        l, r = CONSTRAINTS_MAX - 1, 0

        b = [0] * 100001
        for c in costs:
            b[c] += 1
            l = min(l, c)
            r = max(r, c)
        n = 0
        for c in range(l, r+1):
            while b[c] > 0:
                b[c] -= 1
                coins -= c
                if coins < 0:
                    return n
                n += 1
        return n